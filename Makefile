install:
	uv sync
lint:
	uv run ruff check
test:
	uv run pytest
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml