.PHONY: prepare train chat eval export demo clean

prepare:
	python -m froglm prepare

train:
	python -m froglm train

chat:
	python -m froglm chat

eval:
	python -m froglm eval

export:
	PYTHONPATH=. python scripts/export_onnx.py

demo: export
	python -m http.server 8000 --directory docs

all: prepare train eval export demo

clean:
	rm -rf data/ checkpoints/ docs/model*.onnx* docs/tokenizer.json
