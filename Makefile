install-pipenv:
	sudo pip install pipenv

setup:
	pipenv install --dev

ci: install-pipenv setup black-check mypy test

black:
	pipenv run black archiver

black-check:
	pipenv run black --check archiver

mypy:
	pipenv run mypy --strict archiver

test:
	pipenv run pytest archiver

run:
	pipenv run python -m archiver
