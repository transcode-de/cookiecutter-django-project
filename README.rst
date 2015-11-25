***************************
cookiecutter-django-project
***************************

.. image:: https://img.shields.io/travis/transcode-de/cookiecutter-django-project/master.svg
    :target: https://travis-ci.org/transcode-de/cookiecutter-django-project
    :alt: Build Status

.. image:: https://img.shields.io/requires/github/transcode-de/cookiecutter-django-project.svg
    :target: https://requires.io/github/transcode-de/cookiecutter-django-project/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://badge.waffle.io/transcode-de/cookiecutter-django-project.svg?label=ready&title=issues%20ready
    :target: https://waffle.io/transcode-de/cookiecutter-django-project
    :alt: 'Stories in Ready'

A fully tested `Cookiecutter <https://github.com/audreyr/cookiecutter>`_
template we use for Django projects at `transcode <http://www.transcode.de/>`_.

Batteries included
==================

.. class:: compact

* `Django 1.8 <https://djangoproject.com>`_
* `Initializr 4.0 <http://www.initializr.com/>`_ HTML5 template

    * `Bootstrap 3.1.1 <http://getbootstrap.com/>`_
    * `HTML5 Boilerplate 4.3.0 <http://html5boilerplate.com/>`_
    * `jQuery 1.11.0 <https://jquery.com/>`_

* `django-braces <https://github.com/brack3t/django-braces/>`_
* `django-crispy-forms <https://github.com/maraujop/django-crispy-forms>`_
* `django-grappelli <https://github.com/sehmaschine/django-grappelli>`_
* `django-model-utils <https://github.com/carljm/django-model-utils>`_
* `psycopg2 <http://initd.org/psycopg/>`_
* `Sphinx <http://sphinx-doc.org/>`_

Configuration
-------------

.. class:: compact

* `django-configurations <http://django-configurations.readthedocs.org/>`_
* `dj-database-url <https://github.com/kennethreitz/dj-database-url>`_
* `envdir <http://envdir.readthedocs.org/>`_

Development Tools
-----------------

.. class:: compact

* `bumpversion <https://github.com/peritus/bumpversion>`_
* `django-debug-toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_
* `django-devserver <http://github.com/dcramer/django-devserver>`_

    * `sqlparse <https://github.com/andialbrecht/sqlparse>`_
    * `Werkzeug <http://werkzeug.pocoo.org/>`_

* `Glances <https://github.com/nicolargo/glances>`_
* `IPython <http://ipython.org/>`_
* `pdb++ <https://bitbucket.org/antocuni/pdb/overview>`_
* `pg_activity <https://github.com/julmon/pg_activity>`_

Lint Tools
----------

.. class:: compact

* `check-manifest <https://github.com/mgedmin/check-manifest>`_
* `doc8 <https://github.com/openstack/doc8>`_
* `flake8 <https://gitlab.com/pycqa/flake8>`_
* `isort <https://github.com/timothycrosley/isort>`_
* `pep257 <https://github.com/GreenSteam/pep257>`_

Testing
-------

.. class:: compact

* `coverage <http://nedbatchelder.com/code/coverage/>`_
* `django-coverage-plugin <https://github.com/nedbat/django_coverage_plugin>`_
* `factory_boy <https://pypi.python.org/pypi/factory_boy>`_
* `freezegun <https://github.com/spulec/freezegun>`_
* `pytest <http://pytest.org/>`_
* `pytest-django <http://pytest-django.readthedocs.org/>`_
* `pytest-factoryboy <http://pytest-factoryboy.readthedocs.org/en/latest/>`_
* `tox <http://tox.testrun.org/>`_
* `tox-pyenv <https://github.com/samstav/tox-pyenv>`_

Creating a new Project
======================

First you have to install `Cookiecutter <https://github.com/audreyr/cookiecutter>`_:

::

    $ pip install cookiecutter

After that change to the directory where you want to create a your new Django
project in. Then set up the project using this cookiecutter template like so:

::

    $ cookiecutter gh:transcode-de/cookiecutter-django-project

You have to answer a few questions to configure the project. The defaults are
good for transcode projects - surely you want to override them for your
projects.

Next Steps
==========

Change into your newly created project directory and execute the following
commands to get started.

Install the packages for development:

::

    $ make develop

Then create the new PostgreSQL user and database:

::

    $ make create-db

The next step is to create the Django app(s) you want for the project. Just run
the ``startapp`` task to create new Django app(s):

::

    $ make startapp

Now create the database tables:

::

    $ make migrate

And start the development webserver:

::

    $ make runserver

To see the other targets available in the ``Makefile`` simply run:

::

    $ make

License
=======

This project is licensed under the New BSD License. See ``LICENSE`` for the
full license.
