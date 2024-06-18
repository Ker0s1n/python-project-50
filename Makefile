install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

