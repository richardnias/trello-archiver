install-pipenv:
	sudo pip install pipenv

setup: have-pipenv
	pipenv install --dev

ci: black-check test

black:
	pipenv run black archiver

black-check:
	pipenv run black --check archiver

test:
	pipenv run pytest archiver

run:
	pipenv run python -m archiver
