install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

test: #--cov-report xml - if you need save results
	poetry run pytest --cov=gendiff

lint:
	poetry run flake8

