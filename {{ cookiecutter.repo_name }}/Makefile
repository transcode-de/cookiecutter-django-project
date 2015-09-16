BUILDDIR ?= _build
ENV ?= dev
PORT ?= 8000
SPHINXOPTS =

define CMDS
ifeq ($(1), runserver)
	envdir envs/$(ENV) {{ cookiecutter.pkg_name }}/manage.py$(1)$(PORT)
else
$(1):
	envdir envs/$(ENV) {{ cookiecutter.pkg_name }}/manage.py$(1)
endif
endef

$(eval $(call CMDS, $(cmd)))

.PHONY: help clean clean-build clean-docs clean-pyc clean-test cmd compile-requirements \
	coverage coverage-html create-db develop docs isort migrate open-docs serve-docs runserver \
	shell test test-all test-upload upload

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                    to remove all build, test, coverage and Python artifacts"
	@echo "  clean-build              to remove build artifacts"
	@echo "  clean-docs               to remove documentation artifacts"
	@echo "  clean-pyc                to remove Python file artifacts"
	@echo "  clean-test               to remove test and coverage artifacts"
	@echo "  cmd=<manage.py command>  to use any other manage.py command"
	@echo "  compile-requirements     to update requirements"
	@echo "  coverage                 to generate a coverage report with the default Python"
	@echo "  coverage-html            to generate and open a HTML coverage report with the default Python"
	@echo "  create-db                to create a new PostgreSQL user and database"
	@echo "  develop                  to install (or update) all packages required for development"
	@echo "  dist                     to package a release"
	@echo "  docs                     to build the project documentation as HTML"
	@echo "  isort                    to run isort on the whole project"
	@echo "  migrate                  to synchronize Django's database state with the current set of models and migrations"
	@echo "  open-docs                to open the project documentation in the default browser"
	@echo "  runserver                to start Django's development Web server"
	@echo "  serve-docs               to serve the project documentation in the default browser"
	@echo "  shell                    to start a Python interactive interpreter"
	@echo "  test                     to run unit tests quickly with the default Python"
	@echo "  test-all                 to run unit tests on every Python version with tox"
	@echo "  test-upload              to upload a release to test PyPI using twine"
	@echo "  upload                   to upload a release using twine"


clean: clean-build clean-docs clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-docs:
	$(MAKE) -C docs clean BUILDDIR=$(BUILDDIR)

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .cache/
	rm -fr .tox/
	coverage erase
	rm -fr htmlcov/

cmd:
	@echo "  cmd                       Please use 'make cmd=<manage.py command>'"

compile-requirements:
	pip install git+https://github.com/nvie/pip-tools.git@future
	pip-compile requirements/dev.in
	pip-compile requirements/docs.in
	pip-compile requirements/forks.in
	pip-compile requirements/test.in

coverage:
	coverage run -m pytest $(TEST_ARGS) tests/
	coverage report

coverage-html: coverage
	coverage html
	python -c "import os, webbrowser; webbrowser.open('file://{}/htmlcov/index.html'.format(os.getcwd()))"

create-db:
	createuser -d -e -P {{ cookiecutter.repo_name }}
	createdb -U {{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}

develop:
	pip install -U pip setuptools wheel
	pip install -U -e .
	pip install -U -r requirements/dev.txt

dist: clean
	python setup.py sdist bdist_wheel
	ls -l dist

docs:
	$(MAKE) -C docs html BUILDDIR=$(BUILDDIR) SPHINXOPTS='$(SPHINXOPTS)'

isort:
	isort --recursive setup.py {{ cookiecutter.pkg_name }}/ tests/

migrate:
	envdir envs/$(ENV) {{ cookiecutter.pkg_name }}/manage.py migrate

open-docs:
	python -c "import os, webbrowser; webbrowser.open('file://{}/docs/{}/html/index.html'.format(os.getcwd(), '$(BUILDDIR)'))"

runserver:
	envdir envs/$(ENV) {{ cookiecutter.pkg_name }}/manage.py runserver $(PORT)

serve-docs:
	python -c "import webbrowser; webbrowser.open('http://127.0.0.1:$(PORT)')"
	cd docs/$(BUILDDIR)/html; python -m SimpleHTTPServer $(PORT)

shell:
	envdir envs/$(ENV) {{ cookiecutter.pkg_name }}/manage.py shell

test:
	py.test $(TEST_ARGS) tests/

test-all:
	tox

test-upload:
	twine upload -r test -s dist/*
	python -c "import webbrowser; webbrowser.open('https://testpypi.python.org/pypi/{{ cookiecutter.pkg_name }}')"

upload:
	twine upload -s dist/*
	python -c "import webbrowser; webbrowser.open('https://pypi.python.org/pypi/{{ cookiecutter.pkg_name }}')"
