PROJECT = {{ cookiecutter.repo_name }}
PORT ?= 8000
ENV ?= dev

WHERE = $(shell uname -a)
ifeq ($(CI),true)
PYTHON_PATH = $(BUILD_DIR)/$(PROJECT)
else
PYTHON_PATH = $(shell pwd)/$(PROJECT)
endif

define CMDS
ifeq ($(1), runserver)
	envdir envs/$(ENV) $(PROJECT)/manage.py$(1)$(PORT)
else
$(1):
	envdir envs/$(ENV) $(PROJECT)/manage.py$(1)
endif
endef

$(eval $(call CMDS, $(cmd)))

.PHONY: help clean clean-coverage clean-pyc cmd create-db coverage coverage-html develop docs info \
			isort isort-check migrate runserver shell test upload

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                     to remove all artifacts"
	@echo "  clean-coverage            to remove coverage artifacts"
	@echo "  clean-pyc                 to remove Python file artifacts"
	@echo "  cmd=<manage.py command>   to use any other manage.py command"
	@echo "  coverage                  to generate a coverage report"
	@echo "  coverage-html             to generate and open a HTML coverage report"
	@echo "  create-db                 to create a new PostgreSQL user and database"
	@echo "  develop                   to install all packages required for development"
	@echo "  dist                      to package a release"
	@echo "  docs                      to build and open the project documentation as HTML"
	@echo "  isort                     to run isort on the whole project"
	@echo "  isort-check               to check the whole project with isort"
	@echo "  migrate                   to synchronize Django's database state with the current set of models and migrations"
	@echo "  open-docs                 to open the project documentation in the default browser"
	@echo "  runserver                 to start Django's development Web server"
	@echo "  shell                     to start a Python interactive interpreter"
	@echo "  test                      to run the tests with pytest"
	@echo "  upload                    to upload a release using twine"


clean: clean-coverage clean-pyc

clean-coverage:
	coverage erase
	rm -fr htmlcov

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-release:
	rm -fr release

cmd:
	@echo "  cmd                       Please use 'make cmd=<manage.py command>'"

coverage: info
	PYTHONPATH=$(PYTHON_PATH) py.test --pep8 --flakes $(TEST_ARGS) --cov-config=$(PROJECT)/.coveragerc --cov $(PROJECT) $(PROJECT)

coverage-html: coverage
	coverage html
	@python -c "import os, webbrowser; webbrowser.open('file://%s/htmlcov/index.html' % os.getcwd())"

create-db:
	createuser -d -e -P {{ cookiecutter.repo_name }}
	createdb -U {{ cookiecutter.repo_name }} {{ cookiecutter.repo_name }}

develop:
	pip install --upgrade pip setuptools wheel
	pip install -e .[dev]
	pip install -e .[docs]
	pip install -e .[tests]

dist: clean
	python setup.py sdist bdist_wheel
	ls -l dist

docs:
	$(MAKE) -C docs clean html

info:
	@echo "Testing on $(WHERE)"

isort:
	isort --recursive $(PROJECT)

isort-check:
	isort --check-only --recursive $(PROJECT)

migrate:
	envdir envs/$(ENV) $(PROJECT)/manage.py migrate

open-docs:
	@python -c "import os, webbrowser; webbrowser.open('file://%s/docs/_build/html/index.html' % os.getcwd())"

runserver:
	envdir envs/$(ENV) $(PROJECT)/manage.py runserver $(PORT)

shell:
	envdir envs/$(ENV) $(PROJECT)/manage.py shell

test: info
	PYTHONPATH=$(PYTHON_PATH) py.test --pep8 --flakes $(TEST_ARGS) $(PROJECT)

upload:
	twine upload -s dist/*
