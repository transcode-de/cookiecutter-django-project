.PHONY: help clean clean-backups clean-pyc clean-test develop test

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                    to remove all test and Python artifacts (does not remove backups)"
	@echo "  clean-backups            to remove backup files created by editors and Git"
	@echo "  clean-pyc                to remove Python file artifacts"
	@echo "  clean-test               to remove test artifacts"
	@echo "  develop                  to install (or update) all packages required for development"
	@echo "  test                     to run unit tests on every Python version with tox"


clean: clean-test clean-pyc

clean-backups:
	find . -name '*~' -delete
	find . -name '*.orig' -delete

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '__pycache__' -delete

clean-test:
	rm -fr .cache/
	rm -fr .tox/

develop:
	pip install -U pip setuptools wheel
	pip install -U -r requirements/dev.pip
	pip install -U -r requirements/test-local.pip

test:
	tox
