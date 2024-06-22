install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest --cov=gendiff

lint:
	poetry run flake8

