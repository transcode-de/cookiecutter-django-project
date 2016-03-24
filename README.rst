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

A `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template we use for
Django projects at `transcode <http://www.transcode.de/>`_.

What makes this cookiecutter template special?

* Fully tested cookiecutter template (Python 2, 3 and PyPy)
* The Django project can be build as a Python package, which simplifies
  distribution and installation
* Comes with a simple, modern Django app template
* Up-to-date requirements
* Configured to work with PostgreSQL, including easy creation of user and
  database
* All Django settings can be easily configured for different environments like
  ``dev`` or ``prod`` using environment variables
* Django third-party packages like django-braces, django-crispy-forms,
  django-debug-toolbar, django-model-utils and django-template-debug are
  already installed
* IPython for a powerfull Python and Django shell
* A set of basic Django HTML templates is included
* Includes a ``Makefile`` which helps with all the every-day tasks
* pdb++ and Werkzeug for better debugging
* An extensive collection of lint tools for Python code, documentation and
  packaging
* Prepared for testing with pytest-django, including libraries like faker,
  factory_boy, fauxfactory and freezegun as well as a few useful pytest
  fixtures
* Measuring of test coverage for Python code and Django templates
* A set of tox environments to test the project with different Python versions
  and all lint tools
* pg-activity and Glances to monitor your development machine
* bumpversion makes it easy to increment the version number in several files at
  once with a single command
* Includes configurations for different email backends (SMTP, Mailgun)
* Prepared for reporting to a `Sentry <https://github.com/getsentry/sentry>`_ server
* Comes with a project documentation built with Sphinx using the alabaster
  theme, including pages for installation, settings, releases, deployment and
  contributing

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

    * `sqlparse <https://github.com/andialbrecht/sqlparse>`_
    * `Werkzeug <http://werkzeug.pocoo.org/>`_

* `django-template-debug <https://github.com/calebsmith/django-template-debug>`_
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
* `faker <https://github.com/joke2k/faker>`_
* `fauxfactory <https://github.com/omaciel/fauxfactory>`_
* `freezegun <https://github.com/spulec/freezegun>`_
* `pytest <http://pytest.org/>`_
* `pytest-django <http://pytest-django.readthedocs.org/>`_
* `pytest-factoryboy <http://pytest-factoryboy.readthedocs.org/en/latest/>`_
* `pytest-faker <https://github.com/pytest-dev/pytest-faker>`_
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
good for transcode projects - surely you want to override them for yours.

Next Steps
==========

Change into your newly created project directory and execute the following
commands to get started.

You should create a new virtualenv for the project:

::

    $ mkvirtualenv -a `pwd` my-project


Install the packages for development:

::

    $ make develop

Then create the new PostgreSQL user and database:

::

    $ make create-db-user
    $ make create-db

The next step is to create the Django app(s) you want for the project. Just run
the ``startapp`` task to create new Django app(s):

::

    $ make startapp

Now create the database tables:

::

    $ make migrate

And create a new Django superuser:

::

    $ envdir envs/dev/ python manage.py createsuperuser

Finally start the development webserver:

::

    $ make runserver

To see the other targets available in the ``Makefile`` simply run:

::

    $ make

Detailed installation instructions can be found in your new project under
``docs/installation.rst``.

License
=======

This project is licensed under the New BSD License. See ``LICENSE`` for the
full license.
