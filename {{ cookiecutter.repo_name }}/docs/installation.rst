************
Installation
************

Development Setup
=================

Install the packages for development::

    $ make install-dev

Then create the new PostgreSQL user and database::

    $ make create-db

The next step is to create the Django app(s) you want for the project::

    $ mkdir -p {{ cookiecutter.repo_name }}/<appname>
    $ django-admin startapp <appname> {{ cookiecutter.repo_name }}/<appname>

Now create the database tables::

    $ make migrate

And start the development webserver::

    $ make runserver

To see the other targets available in the ``Makefile`` simply run::

    $ make
