# FrogLM 🐸

A 9M parameter language model trained from scratch to talk like a frog. Built to demystify LLM training - no PhD, no GPU cluster, just one machine and a few minutes.

```plaintext
You> hi frog
Frog> oh hi there. i just hopped over from in the garden.

You> are you hungry
Frog> my tongue is ready. i like crickets best. so crunchy.

You> what is the meaning of life
Frog> sit on pad. eat fly. croak at moon. that is everything.

You> what is bitcoin
Frog> i do not know what bitcoin is. that is beyond the pond.

You> goodnight frog
Frog> goodnight. night is when we frogs sing. the whole pond chorus starts up.
```

---

## Get Started

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python -m froglm prepare    # generate 60K conversations + train tokenizer
python -m froglm train      # ~7 min on Apple Silicon, ~5 min on CUDA
python -m froglm chat       # talk to frog
```

Or run a single prompt:

```bash
python -m froglm chat -p "do you like rain"
```

---

## Browser Demo

After training, export the model and serve locally:

```bash
make demo
```

Opens at `http://localhost:8000`. Runs entirely client-side via WebAssembly - no server, no API keys. The quantized model is ~9MB.

---

## How It Works

FrogLM is a vanilla decoder-only transformer trained on 60K synthetic single-turn conversations. The personality isn't prompted — it's baked into the weights through the training data.

For a full end-to-end walkthrough of every step (with ELI5 explanations), see **[HOW_IT_WORKS.md](HOW_IT_WORKS.md)**.

| Data | Value |
| - | - |
| Parameters | 8.7M |
| Layers | 6 |
| Hidden dim | 384 |
| Heads | 6 |
| FFN | 768 (ReLU) |
| Vocab | 4,096 BPE tokens |
| Context | 128 tokens |
| Position | Learned embeddings |
| LM head | Weight-tied |

No GQA, no RoPE, no SwiGLU. Standard attention + LayerNorm + ReLU FFN.

---

## The Frog

An amphibian - lives in the pond and on land.

- Short, lowercase sentences
- Hunts bugs with a fast sticky tongue
- Active at night - croaks in a chorus
- Hibernates in mud, awakens in spring
- Hops between the pond and the garden
- Doesn't understand human abstractions
- Thinks about bugs constantly

61 topics covering greetings, food, rain, jumping, predators, seasons, philosophy, dreams, farewells, confused/off-topic deflection, and more.

---

## Data

60K synthetic conversations generated via template composition. Each topic has a response generator that combines randomized vocabulary pools (22 bug types, 23 pond objects, 18 land objects, 31 activities) to produce unique outputs at scale.

Format:

```plaintext
<|im_start|>user
hi frog<|im_end|>
<|im_start|>assistant
ribbit. the pond is calm today.<|im_end|>
```

---

## Project Layout

```plaintext
froglm/
├── config.py                # FrogConfig + TrainConfig
├── device.py                # CUDA / MPS / CPU detection
├── train.py                 # Training loop with eval + checkpointing
├── inference.py             # FrogInference class + chat CLI
├── model/
│   ├── attention.py         # Multi-head attention + FFN
│   ├── block.py             # Transformer block
│   └── lm.py                # FrogLM model
├── data/
│   ├── vocabulary.py        # Word pools + helpers
│   ├── personality.py       # Frog response generators
│   ├── user_prompts.py      # User input generators
│   ├── topics.py            # Topic registry
│   ├── generator.py         # Dataset generation
│   ├── tokenizer.py         # BPE tokenizer training
│   └── dataset.py           # DataLoader + dynamic padding
├── eval/
│   ├── cases.py             # Personality test cases
│   └── runner.py            # Eval runner

scripts/
└── export_onnx.py           # ONNX export + quantization

docs/
├── index.html               # Browser demo
├── model_q.onnx             # Quantized model (~9MB)
└── tokenizer.json           # BPE tokenizer
```

---

## All Commands

| Command | What it does |
| - | - |
| `python -m froglm prepare` | Generate data + train tokenizer |
| `python -m froglm train` | Train model (best saved to `checkpoints/`) |
| `python -m froglm chat` | Interactive chat |
| `python -m froglm chat -p "..."` | Single prompt |
| `python -m froglm eval` | Run personality eval cases |
| `make export` | Export ONNX + quantize |
| `make demo` | Export + serve browser demo |

---

## Why These Choices

**Amphibian.** A frog lives on land and water. Richer worldview - gardens, rain, hibernation, night choruses.

**No system prompt.** Personality is in the weights. A 9M model can't follow conditional instructions anyway.

**Single-turn only.** 128-token context degrades at turn 3-4. A forgetful frog is fine. Garbled output isn't.

**Synthetic data.** Template composition with randomized components gives consistent personality with enough variety to generalize.

**Vanilla transformer.** Fancy attention variants don't help at 9M params. Simple code, same quality.

---

## License

MIT
