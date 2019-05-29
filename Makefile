ci: black test

black:
	pipenv run black archiver

test:
	pipenv run pytest archiver

run:
	pipenv run archiver/main.py
