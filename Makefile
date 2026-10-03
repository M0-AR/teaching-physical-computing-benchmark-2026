.PHONY: setup run test docker-build docker-run figs clean

setup:
	pip install -r requirements.txt

run:
	PYTHONPATH=src python experiments/06_reproduce_all.py

test:
	PYTHONPATH=src pytest -v

docker-build:
	docker compose build

docker-run:
	docker compose up --build

figs:
	PYTHONPATH=src python experiments/05_hidden_patterns.py

clean:
	rm -rf results/figures/*.png results/tables/*.csv data/processed/*.csv __pycache__
