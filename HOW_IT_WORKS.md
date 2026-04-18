# How FrogLM Works - End to End

This document explains every step of building FrogLM, from raw idea to a working chatbot in your browser.

---

## The Big Picture

```plaintext
[Idea: "frog personality"]
        ↓
[Generate 60K fake conversations]
        ↓
[Train a tokenizer on those conversations]
        ↓
[Train a neural network to predict the next token]
        ↓
[Chat: feed it a prompt, let it generate tokens one by one]
        ↓
[Export to ONNX → run in browser via WebAssembly]
```

That's it. Every LLM works this way - the only difference between FrogLM and GPT-4 is scale.

---

## Step 1: Define the Personality

Before writing any code, we decide who the frog is:

- Speaks in short, lowercase sentences
- Knows about: the pond, bugs, mud, rain, lily pads, jumping, croaking, the garden
- Doesn't know about: bitcoin, phones, politics, math, human stuff
- Personality: chill, a little dumb, obsessed with bugs

This matters because the personality lives in the **training data**, not in a system prompt. The model will learn to be a frog by seeing 60,000 examples of frog-like responses.

---

## Step 2: Generate Training Data

**File:** `froglm/data/personality.py`, `user_prompts.py`, `vocabulary.py`

We write template generators for 61 topics. Each generator picks random words from vocabulary pools and assembles a response:

```python
def _frog_food():
    starters = ["yes. always yes.", "my tongue is ready.", ...]
    middles = [f"i like {pick(BUG_TYPES)}s best. so crunchy.", ...]
    return join_sentences(pick(starters), pick(middles))
```

**ELI5:** Imagine a mad-libs book for frogs. "My tongue is ready. I like ___s best." Fill in the blank with a random bug. Do this 60,000 times across 61 different conversation topics.

The output is 60K pairs like:

```json
{"input": "are you hungry", "output": "my tongue is ready. i like crickets best. so crunchy."}
```

These get formatted into a chat template:

```plaintext
<|im_start|>user
are you hungry<|im_end|>
<|im_start|>assistant
my tongue is ready. i like crickets best. so crunchy.<|im_end|>
```

**Why this format?** The `<|im_start|>` and `<|im_end|>` tokens tell the model where the user's message ends and where the frog's response begins. Without them, the model wouldn't know when to stop generating.

---

## Step 3: Train a Tokenizer

**File:** `froglm/data/tokenizer.py`

Neural networks don't understand text - they understand numbers. A tokenizer converts text into a sequence of integer IDs.

We train a **BPE (Byte Pair Encoding)** tokenizer on our 60K conversations. It learns which character sequences appear frequently and merges them into single tokens:

```plaintext
"croaking" → ["cro", "aking"] → [token_412, token_87]
"the pond" → ["the", " pond"] → [token_52, token_139]
```

**ELI5:** Imagine you're creating a codebook. Common words like "the", "pond", "bug" get their own code number. Rare words get split into pieces that each have a code. Our codebook has ~2,600 entries.

**Why BPE?** It handles any text - even words it's never seen - by falling back to character-level pieces. A vocabulary of 4,096 is enough for our tiny frog world.

---

## Step 4: The Model Architecture

**File:** `froglm/model/lm.py`, `attention.py`, `block.py`

FrogLM is a **decoder-only transformer** - the same architecture as GPT, just much smaller.

```plaintext
Input tokens: [1, 71, 47, 428, 113, 61, 861, 2]
                          ↓
              ┌─────────────────────┐
              │   Token Embedding   │  Convert each ID to a 384-dim vector
              │   + Position Emb    │  Add "where am I in the sequence" info
              └─────────────────────┘
                          ↓
              ┌─────────────────────┐
              │  Transformer Block  │ ×6 (attention + feed-forward)
              └─────────────────────┘
                          ↓
              ┌─────────────────────┐
              │      LM Head        │  Predict probability of next token
              └─────────────────────┘
                          ↓
Output: probability distribution over 4,096 possible next tokens
```

### What's inside each Transformer Block?

1. **Multi-Head Attention** - lets each token look at all previous tokens to understand context. "What words came before me that are relevant?"

2. **Feed-Forward Network (FFN)** - a simple two-layer neural net that processes each token independently. This is where the model stores "knowledge."

3. **LayerNorm + Residual connections** - keeps training stable.

**ELI5:** Imagine reading a sentence word by word. Attention is like glancing back at earlier words to understand what the current word means. The FFN is like your brain processing that understanding. Do this 6 times (6 layers) and you get a pretty good guess at what word comes next.

### Key numbers

- 384-dimensional vectors (each token is represented as 384 numbers)
- 6 attention heads (6 different "perspectives" looking at context)
- 6 layers (6 rounds of attention + processing)
- 8.7M total parameters (weights the model learns during training)

### Causal Mask

The model can only look at tokens that came BEFORE the current position - never forward. This is enforced by a triangular mask:

```plaintext
Token 1 can see: [1]
Token 2 can see: [1, 2]
Token 3 can see: [1, 2, 3]
...
```

**ELI5:** When writing a story, you can reference what you already wrote, but you can't peek at what comes next. The mask enforces this rule.

### Weight Tying

The token embedding matrix (input) and the LM head matrix (output) share the same weights. This means "the representation of a word" and "the prediction of a word" use the same parameters - halving memory usage for those layers.

---

## Step 5: Training

**File:** `froglm/train.py`

Training = showing the model millions of examples and adjusting its weights to get better at predicting the next token.

### The Training Loop

```plaintext
For each batch of conversations:
    1. Tokenize: "ribbit. the pond is calm." → [412, 52, 139, 80, 612]
    2. Input:  [412, 52, 139, 80]     (all tokens except last)
    3. Target: [52, 139, 80, 612]     (all tokens except first)
    4. Model predicts next token at each position
    5. Compare predictions to targets → compute loss
    6. Backpropagate: adjust weights to reduce loss
    7. Repeat 10,000 times
```

**ELI5:** Show the model "ribbit. the pond is" and ask "what comes next?" It guesses. If it's wrong, nudge the weights slightly toward the right answer. Do this millions of times and it learns the pattern.

### Key Training Details

- **AdamW optimizer** - the algorithm that decides how to adjust weights. Better than basic gradient descent.
- **Cosine learning rate schedule** - start with big adjustments, gradually make smaller ones. Like tuning a radio: big turns first, then fine-tuning.
- **Warmup** - for the first 200 steps, slowly increase the learning rate. Prevents the model from making wild jumps at the start.
- **Gradient clipping** - if an adjustment would be too large, cap it. Prevents training from exploding.
- **Eval every 200 steps** - test on held-out data to check if the model is actually learning (not just memorizing).

### Loss

The loss number tells you how wrong the model's predictions are. Lower = better.

```plaintext
Step 0:     loss = 8.37  (random guessing)
Step 1000:  loss = 0.50  (getting good)
Step 10000: loss = 0.38  (converged)
```

**ELI5:** If loss is 8, the model is clueless. If loss is 0.38, it's pretty confident about what comes next in a frog conversation.

---

## Step 6: Inference (Chat)

**File:** `froglm/inference.py`

Once trained, we generate text **one token at a time**:

```plaintext
1. Format prompt: "<|im_start|>user\nhi frog<|im_end|>\n<|im_start|>assistant\n"
2. Encode to token IDs
3. Feed to model → get probability distribution over next token
4. Sample from that distribution (with temperature + top-k)
5. Append sampled token to sequence
6. Repeat from step 3 until <|im_end|> token or max length
7. Decode token IDs back to text
```

### Temperature

Controls randomness. Lower = more predictable, higher = more creative.

- `temperature=0.0` → always pick the most likely token (boring, repetitive)
- `temperature=0.7` → mostly likely tokens but with some variety (what we use)
- `temperature=1.5` → very random (might produce nonsense)

**ELI5:** Temperature is like asking "how adventurous should the frog be?" Low = always says the same thing. High = says weird stuff. 0.7 = just right.

### Top-k Sampling

Only consider the top 40 most likely next tokens. Ignore everything else. This prevents the model from occasionally picking a wildly unlikely token.

**ELI5:** Instead of choosing from ALL 4,096 possible next words, only consider the 40 best options. Eliminates garbage.

---

## Step 7: ONNX Export + Browser Demo

**File:** `scripts/export_onnx.py`, `docs/index.html`

### Export

PyTorch models can't run in a browser. We convert to ONNX (Open Neural Network Exchange) - a universal format - then quantize the weights from 32-bit floats to 8-bit integers:

```plaintext
PyTorch model (33MB) → ONNX → Quantized ONNX (8.6MB)
```

**ELI5:** The model's "brain" is stored as very precise numbers (32-bit). We round them to less precise numbers (8-bit) - the frog gets slightly dumber but the file is 4x smaller. For a toy model, the quality difference is negligible.

### Browser Demo

The `docs/index.html` file loads:

1. **ONNX Runtime Web** - a library that runs ONNX models in the browser using WebAssembly
2. **model_q.onnx** - the quantized model (~9MB download)
3. **tokenizer.json** - the BPE tokenizer vocabulary and merge rules

The JavaScript reimplements the same tokenizer and generation loop that Python does. The model runs entirely on your CPU via WASM - nothing is sent to any server.

**ELI5:** We took the frog's brain, shrunk it, and put it inside your web browser. When you type a message, your computer does all the thinking locally. No internet needed after the initial download.

---

## Why It Works (and Why It's Limited)

### Why it works

- 60K examples is enough for a 9M model to memorize the frog's personality
- Template composition gives enough variety that it generalizes to unseen phrasings
- The chat format (`<|im_start|>user...assistant`) teaches it the turn-taking pattern

### Why it's limited

- 128-token context = can't do multi-turn conversations well
- 9M params = can't reason, can't follow complex instructions
- Synthetic data = responses are combinations of templates, not truly creative
- Single personality = can't switch characters or follow system prompts

### What you'd need for a "real" LLM

- Billions of parameters (not millions)
- Trillions of tokens of training data (not 60K conversations)
- Months of GPU time (not 7 minutes)
- RLHF or DPO for alignment (not just next-token prediction)

But the fundamental mechanism - predict the next token, over and over - is identical from FrogLM to GPT-4.

---

## File Flow Summary

```plaintext
vocabulary.py          → defines the frog's world (bugs, ponds, activities)
personality.py         → generates frog responses using vocabulary
user_prompts.py        → generates human inputs
topics.py              → pairs them into (input, output) samples
generator.py           → produces 60K samples as JSONL
tokenizer.py           → trains BPE tokenizer on the JSONL
dataset.py             → loads JSONL + tokenizes for PyTorch
model/lm.py            → the transformer that learns from the data
train.py               → the training loop
inference.py           → loads trained model + generates responses
scripts/export_onnx.py → converts to browser-friendly format
docs/index.html        → runs it all in your browser
```

Each file does one thing. The whole pipeline is ~2,000 lines of Python + 200 lines of JS.
