.PHONY: frog-prepare frog-train frog-chat frog-eval frog-export frog-demo
.PHONY: cat-prepare cat-train cat-chat cat-eval cat-export cat-demo
.PHONY: clean

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

frog-demo: frog-export
	python -m http.server 8000 --directory docs/frog

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

cat-demo: cat-export
	python -m http.server 8001 --directory docs/cat

# ── Cleanup ──
clean:
	rm -rf data/ checkpoints/ docs/frog/model* docs/frog/tokenizer.json docs/cat/model* docs/cat/tokenizer.json
