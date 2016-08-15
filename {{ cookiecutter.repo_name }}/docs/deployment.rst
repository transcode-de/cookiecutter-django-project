**********
Deployment
**********

.. note::

    You should extend this chapter with instructions explaining how to deploy
    your project and how to install and configure the WSGI and HTTP server(s).
    Make sure that you configure the WSGI server to use the right envdir!

Install the project package and extra requirements
==================================================

First install the ``{{ cookiecutter.pkg_name }}`` package. It is very useful
to use a virtualenv for that, there are several good reasons for it. Read the
blog posts `virtualenv Lives! <https://hynek.me/articles/virtualenv-lives/>`_
by Hynek Schlawack and `Fast Immutable Python Deployments
<https://lincolnloop.com/blog/fast-immutable-python-deployments/>`_ by Peter
Baumgartner to gain a better understanding of the reasons.

::

    $ pip install {{ cookiecutter.pkg_name }}

If you are using `Mailgun <https://www.mailgun.com/>`_ install the extra
requirements as well:

::

    $ pip install {{ cookiecutter.pkg_name }}[mailgun]

If you are using `Sentry <https://getsentry.com/>`_ you have to do the same for
``raven``:

::

    $ pip install {{ cookiecutter.pkg_name }}[raven]

Configure the project environment
=================================

`envdir <https://pypi.python.org/pypi/envdir>`_ is used to configure the
project's environment.

Let's assume we want to deploy a production site. The first step is to create a
:file:`prod` directory which will contain all the files defining the
environment variables:

::

    $ mkdir -p envs/prod

Now create a file to define the configuration class to be used:

::

    $ echo "Production" > envs/prod/DJANGO_CONFIGURATION

Then create the file for the ``DJANGO_SETTINGS_MODULE`` environment variable:

::

    $ echo "{{ cookiecutter.pkg_name }}.config.settings.public" > envs/prod/DJANGO_SETTINGS_MODULE

Now configure the rest of the settings for your Django project. You should make
sure that the following environment variables are set to right values.

* ``DJANGO_SECRET_KEY``
* ``DJANGO_ALLOWED_HOSTS``
* ``DEFAULT_DATABASE_URL``
* ``DJANGO_MEDIA_ROOT``
* ``DJANGO_STATIC_ROOT``
* ``DJANGO_TIME_ZONE``
* ``DJANGO_DEFAULT_FROM_EMAIL``
* ``DJANGO_ADMINS``
* ``DJANGO_SILENCED_SYSTEM_CHECKS``

You should not set ``DJANGO_DEBUG`` as the default value is ``False`` by
default which is the right value for production sites.

Don't forget to configure the email backend you selected.

Also configure ``DJANGO_RAVEN_CONFIG_DSN`` if you want to use Sentry for
logging.

Have a look at :doc:`settings` to understand what each setting does.

Now set the environment's name so that our :file:`Makefile` will use the right
environment:

::

    $ export ENV=prod

.. note::

    If you want to keep the ``ENV`` variable at this value add it to the
    :file:`.bashrc`:

    ::

        $ echo "export ENV=prod" >> ~/.bashrc

Migrate the database
====================

Then migrate the database:

::

    $ make migrate

Run the deployment checks
=========================

Now run the deployment checks:

::

    $ envdir envs/prod python manage.py check --deploy

No security issues should be identified. Otherwise check your configuration or
change ``DJANGO_SILENCED_SYSTEM_CHECKS``.

Create a new superuser
======================

After that create a new superuser:

::

    $ envdir envs/prod python manage.py createsuperuser

Create and fill the directories for user uploads and static files
=================================================================

Finally create the ``MEDIA_ROOT`` and ``STATIC_ROOT`` directories and collect
the static files into the ``STATIC_ROOT`` directory:

::

    $ envdir envs/prod python manage.py collectstatic
