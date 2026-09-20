install:
	python -m pip install -r requirements.txt
test:
	pytest -q
notebook:
	jupyter lab
clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
