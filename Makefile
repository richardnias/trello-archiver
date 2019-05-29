ci: black test

black:
	pipenv run black .

test:
	pipenv run pytest

run:
	pipenv run main.py
