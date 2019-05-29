ci: black test

black:
	pipenv run black

test:
	PIPENV_DOTENV_LOCATION=.env.test pipenv run pytest

run:
	pipenv run main.py
