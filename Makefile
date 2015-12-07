PORT ?= 8000

.PHONY: help clean clean-backups clean-pyc clean-test develop test

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                    to remove all test and Python artifacts (does not remove backups)"
	@echo "  clean-backups            to remove backup files created by editors and Git"
	@echo "  clean-pyc                to remove Python file artifacts"
	@echo "  clean-test               to remove test artifacts"
	@echo "  develop                  to install (or update) all packages required for development"
	@echo "  isort                    to run isort on the whole project"
	@echo "  open-project-docs        to open the project documentation in the default browser"
	@echo "  serve-project-docs       to serve the project documentation in the default browser"
	@echo "  test                     to run unit tests on every Python version with tox"


clean: clean-test clean-pyc

clean-backups:
	find . -name '*~' -delete
	find . -name '*.orig' -delete
	find . -name '*.swp' -delete

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '__pycache__' -delete

clean-test:
	rm -fr .cache/
	rm -fr .tox/

develop:
	pip install -U pip setuptools wheel
	pip install -U -r requirements/dev.pip -r requirements/test-local.pip

isort:
	isort --recursive hooks/

open-project-docs:
	python -c "import os, webbrowser; webbrowser.open('file://{}/.tox/project-docs/tmp/my-project/.tox/docs/tmp/html/index.html'.format(os.getcwd()))"

serve-project-docs:
	python -c "import webbrowser; webbrowser.open('http://127.0.0.1:$(PORT)')"
	cd .tox/project-docs/tmp/my-project/.tox/docs/tmp/html/; python -m http.server $(PORT)

test:
	tox
