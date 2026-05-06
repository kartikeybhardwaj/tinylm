# TinyLM 🐸🐱

Train tiny language models with distinct personalities from scratch. Each model is ~9M parameters, trains in minutes on a single GPU, and runs in the browser.

```plaintext
You> hi frog                          You> hi cat
Frog> oh hi there. i just hopped      Cat> oh. it is you. i was busy
over from the garden.                 ignoring you.

You> what is bitcoin                  You> what is bitcoin
Frog> i do not know what bitcoin      Cat> is bitcoin edible. no.
is. that is beyond the pond.          then i do not care.

You> goodnight                        You> goodnight
Frog> goodnight. night is when we     Cat> the humans are sleeping.
frogs sing. the whole pond chorus     this is when i come alive. time
starts up.                            to run through the house.
```

---

## Get Started

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Train a Frog

```bash
python -m froglm prepare    # generate 60K conversations + train tokenizer
python -m froglm train      # ~7 min on Apple Silicon, ~5 min on CUDA
python -m froglm chat       # talk to frog
```

### Train a Cat

```bash
python -m catlm prepare
python -m catlm train
python -m catlm chat
```

Single prompt mode:

```bash
python -m froglm chat -p "do you like rain"
python -m catlm chat -p "do you like dogs"
```

---

## Browser Demo

A single page serves every personality. Export the model(s) you want, then run the demo:

```bash
make frog-export   # writes docs/frog/{model_q.onnx,tokenizer.json}
make cat-export    # writes docs/cat/{model_q.onnx,tokenizer.json}
make demo          # http://localhost:8000
```

The page reads `docs/manifest.json` to populate a personality dropdown. Use `?p=frog` or `?p=cat` to deep-link. To add a new personality to the demo, add an entry to `manifest.json` after exporting — no HTML changes needed.

Runs entirely client-side via WebAssembly — no server, no API keys. Each quantized model is ~9MB.

---

## How It Works

Each personality is a vanilla decoder-only transformer trained on 60K synthetic single-turn conversations. The personality isn't prompted — it's baked into the weights through the training data.

For a full end-to-end walkthrough of every step (with ELI5 explanations), see **[HOW_IT_WORKS.md](HOW_IT_WORKS.md)**.

| | |
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

## Architecture

```plaintext
core/                            # Shared engine (model, training, inference)
├── config.py                    # ModelConfig + TrainConfig
├── device.py                    # CUDA / MPS / CPU detection
├── train.py                     # Training loop with eval + checkpointing
├── inference.py                 # LMInference class
├── model/
│   ├── attention.py             # Multi-head attention + FFN
│   ├── block.py                 # Transformer block
│   └── lm.py                    # TinyLM model
├── data/
│   ├── dataset.py               # DataLoader + dynamic padding
│   ├── generator.py             # Dataset generation
│   └── tokenizer.py             # BPE tokenizer training
└── eval/
    └── runner.py                # Eval runner

froglm/                          # 🐸 Frog personality
├── __main__.py                  # python -m froglm
└── data/
    ├── vocabulary.py            # Pond, bugs, mud, garden
    ├── personality.py           # Frog response generators (61 topics)
    ├── user_prompts.py          # User input generators
    ├── topics.py                # Topic registry
    └── eval_cases.py            # Personality test cases

catlm/                           # 🐱 Cat personality
├── __main__.py                  # python -m catlm
└── data/
    ├── vocabulary.py            # House, furniture, prey, threats
    ├── personality.py           # Cat response generators (48 topics)
    ├── user_prompts.py          # User input generators
    ├── topics.py                # Topic registry
    └── eval_cases.py            # Personality test cases

scripts/
└── export_onnx.py               # ONNX export + quantization

docs/
├── frog/                        # Frog browser demo
└── cat/                         # Cat browser demo
```

---

## Adding a New Personality

1. Create a new directory (e.g. `doglm/data/`)
2. Write `vocabulary.py` — word pools for the animal's world
3. Write `personality.py` — response generators
4. Write `user_prompts.py` — user input generators
5. Write `topics.py` — wire generators into `ALL_TOPICS`
6. Write `eval_cases.py` — personality test cases
7. Create `__main__.py` — copy from froglm/catlm, change `NAME`

That's it. The core engine handles everything else.

---

## All Commands

| Command | What it does |
| - | - |
| `python -m froglm prepare` | Generate frog data + train tokenizer |
| `python -m froglm train` | Train frog model |
| `python -m froglm chat` | Chat with frog |
| `python -m froglm chat -p "..."` | Single prompt |
| `python -m froglm eval` | Run frog eval cases |
| `python -m catlm prepare` | Generate cat data + train tokenizer |
| `python -m catlm train` | Train cat model |
| `python -m catlm chat` | Chat with cat |
| `python -m catlm eval` | Run cat eval cases |
| `make frog-export` | Export frog ONNX + quantize → `docs/frog/` |
| `make cat-export` | Export cat ONNX + quantize → `docs/cat/` |
| `make demo` | Serve unified browser demo at `http://localhost:8000` |

---

## Why These Choices

**Shared core, separate personalities.** The transformer, training loop, tokenizer, and inference are identical for every personality. Only the training data differs. This means adding a new animal is just writing templates — no ML code needed.

**No system prompt.** Personality is in the weights. A 9M model can't follow conditional instructions anyway.

**Single-turn only.** 128-token context degrades at turn 3-4. A forgetful pet is fine. Garbled output isn't.

**Synthetic data.** Template composition with randomized components gives consistent personality with enough variety to generalize.

**Vanilla transformer.** Fancy attention variants don't help at 9M params. Simple code, same quality.

---

## License

MIT
