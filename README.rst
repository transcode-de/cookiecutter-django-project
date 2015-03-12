***************************
cookiecutter-django-project
***************************

.. image:: https://badge.waffle.io/transcode-de/cookiecutter-django-project.svg?label=ready&title=issues%20ready 
 :target: https://waffle.io/transcode-de/cookiecutter-django-project 
 :alt: 'Stories in Ready'

A `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template we
use for Django projects at `transcode <http://www.transcode.de/>`_.

Batteries included
==================

* `Django 1.7 <https://djangoproject.com>`_
* `Initializr 4.0 <http://www.initializr.com/>`_ HTML5 template

    * `Bootstrap 3.1.1 <http://getbootstrap.com/>`_
    * `HTML5 Boilerplate 4.3.0 <http://html5boilerplate.com/>`_
    * `jQuery 1.11.0 <https://jquery.com/>`_

* `django-braces <https://github.com/brack3t/django-braces/>`_
* `django-crispy-forms <https://github.com/maraujop/django-crispy-forms>`_
* `django-grappelli <https://github.com/sehmaschine/django-grappelli>`_
* `psycopg2 <http://initd.org/psycopg/>`_
* `Sphinx <http://sphinx-doc.org/>`_

Configuration
-------------

* `django-configurations <http://django-configurations.readthedocs.org/>`_
* `dj-database-url <https://github.com/kennethreitz/dj-database-url>`_
* `envdir <http://envdir.readthedocs.org/>`_

Development Tools
-----------------

* `bumpversion <https://github.com/peritus/bumpversion>`_
* `django-debug-toolbar <https://github.com/django-debug-toolbar/django-debug-toolbar>`_
* `django-devserver <http://github.com/dcramer/django-devserver>`_

    * `sqlparse <https://github.com/andialbrecht/sqlparse>`_
    * `Werkzeug <http://werkzeug.pocoo.org/>`_

* `IPython <http://ipython.org/>`_
* `ipdb <https://github.com/gotcha/ipdb>`_
* `pg_activity <https://github.com/julmon/pg_activity>`_

Testing
-------

* `check-manifest <https://github.com/mgedmin/check-manifest>`_
* `coverage <http://nedbatchelder.com/code/coverage/>`_
* `factory_boy <https://pypi.python.org/pypi/factory_boy>`_
* `flake8 <https://gitlab.com/pycqa/flake8>`_
* `freezegun <https://github.com/spulec/freezegun>`_
* `isort <https://github.com/timothycrosley/isort>`_
* `pytest <http://pytest.org/>`_
* `pytest-django <http://pytest-django.readthedocs.org/>`_
* `pytest-pythonpath <https://github.com/bigsassy/pytest-pythonpath>`_
* `tox <http://tox.testrun.org/>`_

Creating a new Project
======================

First you have to install `Cookiecutter <https://github.com/audreyr/cookiecutter>`_::

    $ pip install cookiecutter

After that change to the directory where you want to create a your new
Django project in. Then set up the project using this cookiecutter
template like so::

    $ cookiecutter https://github.com/transcode-de/cookiecutter-django-project.git

You have to answer a few questions to configure the project. The
defaults are good for transcode projects - surely you want to override
them for your projects.

Next Steps
==========

Change into your newly created project directory and execute the
following commands to get started.

Install the packages for development::

    $ make develop

Then create the new PostgreSQL user and database::

    $ make create-db

The next step is to create the Django app(s) you want for the project::

    $ mkdir -p <projectname>/<appname>
    $ django-admin startapp <appname> <projectname>/<appname>

Now create the database tables::

    $ make migrate

And start the development webserver::

    $ make runserver

To see the other targets available in the ``Makefile`` simply run::

    $ make

License
=======

This project is licensed under the New BSD License. See ``LICENSE`` for
the full license.
