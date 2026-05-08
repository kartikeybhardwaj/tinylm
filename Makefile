.PHONY: frog-prepare frog-train frog-chat frog-eval frog-export
.PHONY: cat-prepare cat-train cat-chat cat-eval cat-export
.PHONY: fish-prepare fish-train fish-chat fish-eval fish-export
.PHONY: demo clean

# ── Frog ──
frog-prepare:
	python -m froglm prepare

frog-train:
	python -m froglm train

frog-chat:
	python -m froglm chat

frog-eval:
	python -m froglm eval

frog-export:
	PYTHONPATH=. python scripts/export_onnx.py frog

# ── Cat ──
cat-prepare:
	python -m catlm prepare

cat-train:
	python -m catlm train

cat-chat:
	python -m catlm chat

cat-eval:
	python -m catlm eval

cat-export:
	PYTHONPATH=. python scripts/export_onnx.py cat

# ── Fish ──
fish-prepare:
	python -m fishlm prepare

fish-train:
	python -m fishlm train

fish-chat:
	python -m fishlm chat

fish-eval:
	python -m fishlm eval

fish-export:
	PYTHONPATH=. python scripts/export_onnx.py fish

# ── Browser demo (serves all personalities at http://localhost:8000) ──
demo:
	python -m http.server 8000 --directory docs

# ── Cleanup ──
clean:
	rm -rf data/ checkpoints/ docs/frog/model* docs/frog/tokenizer.json docs/cat/model* docs/cat/tokenizer.json docs/fish/model* docs/fish/tokenizer.json
