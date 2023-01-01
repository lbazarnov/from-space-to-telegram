install:
	poetry install

brain-games:
	poetry run from-space-to-telegram

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 from_space_to_telegram