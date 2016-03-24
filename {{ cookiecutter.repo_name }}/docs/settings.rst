********
Settings
********

This is a list of all settings for this project. Each setting can be configured
using environment variables.

.. Keep the length of the "Description" column at a maximum of 45 characters.

These are the default settings in :file:`{{ cookiecutter.repo_name }}/manage.py`.
Both together control which settings are loaded and used.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``DJANGO_CONFIGURATION``
      - ``'Development'``
      - ``DJANGO_CONFIGURATION``
      - | Name of the `django-configurations <https://github.com/jazzband/django-configurations>`_
        | class you want to use.
    * - ``DJANGO_SETTINGS_MODULE``
      - ``'{{ cookiecutter.pkg_name }}.config.settings.dev'``
      - ``DJANGO_SETTINGS_MODULE``
      - | Python path to the settings module
        | for this project.

General Settings
================

List of general Django settings from
:py:class:`{{ cookiecutter.pkg_name }}.config.settings.common.Common`.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``ADMINS``
      - ``(('transcode', 'errors@example.com'),)``
      - ``DJANGO_ADMINS``
      - | A tuple that lists people who get
        | code error notifications. When
        | ``DEBUG=False`` and a view raises
        | an exception, Django will email
        | these people with the full
        | exception information.
        | Example environment value:
        | ``Alice,alice@brown.com;Bob,bob@dylan.com``
    * - ``ALLOWED_HOSTS``
      - ``['{{ cookiecutter.domain }}']``
      - ``DJANGO_ALLOWED_HOSTS``
      - | A list of strings representing the
        | host/domain names that this Django
        | site can serve.
        | Example environment value:
        | ``example.com,www.example.com``
    * - ``CACHES``
      - | ``{``
        | ``'default': {``
        | ``'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',``
        | ``}``
        | ``}``
      - ``DJANGO_CACHES``
      - | A dictionary containing the
        | settings for all caches to be used
        | with Django.
    * - ``CRISPY_TEMPLATE_PACK``
      - ``'bootstrap3'``
      - ``DJANGO_CRISPY_TEMPLATE_PACK``
      - | The default template pack to be
        | used by `django-crispy-forms <https://github.com/maraujop/django-crispy-forms>`_.
    * - ``DEBUG``
      - ``False``
      - ``DJANGO_DEBUG``
      - | A boolean that turns on/off debug
        | mode. Never deploy a site into
        | production with ``DEBUG`` turned
        | on.
    * - ``DEFAULT_FROM_EMAIL``
      - ``'noreply@example.com'``
      - ``DJANGO_DEFAULT_FROM_EMAIL``
      - | Default email address to use for
        | various automated correspondence.
    * - ``DJANGO_TEMPLATES_STRING_IF_INVALID``
      - ``''``
      - ``DJANGO_DJANGO_TEMPLATES_STRING_IF_INVALID``
      - | The output, as a string, that
        | Django's template engine should
        | use for invalid (e.g. misspelled)
        | variables.
    * - ``DJANGO_TEMPLATES_TEMPLATE_DEBUG``
      - ``False``
      - ``DJANGO_DJANGO_TEMPLATES_TEMPLATE_DEBUG``
      - | A boolean that turns on/off template debug
        | mode for Django's template engine.
    * - ``LANGUAGE_CODE``
      - ``'en-us'``
      - ``DJANGO_LANGUAGE_CODE``
      - | A string representing the
        | language code for this
        | installation.
    * - ``MIDDLEWARE_CLASSES``
      - | ``['django.contrib.sessions.middleware.SessionMiddleware',``
        | ``'django.middleware.common.CommonMiddleware',``
        | ``'django.middleware.csrf.CsrfViewMiddleware',``
        | ``'django.contrib.auth.middleware.AuthenticationMiddleware',``
        | ``'django.contrib.auth.middleware.SessionAuthenticationMiddleware',``
        | ``'django.contrib.messages.middleware.MessageMiddleware',``
        | ``'django.middleware.clickjacking.XFrameOptionsMiddleware',``
        | ``'django.middleware.security.SecurityMiddleware',]``
      - ``DJANGO_MIDDLEWARE_CLASSES``
      - | A list of middleware classes to
        | use.
    * - ``MEDIA_ROOT``
      - ``'<full path to {{ cookiecutter.pkg_name }}>/media/'``
      - ``DJANGO_MEDIA_ROOT``
      - | Absolute filesystem path to the
        | directory that will hold
        | user-uploaded files. Must be
        | changed for production sites.
    * - ``MEDIA_URL``
      - ``'/media/'``
      - ``DJANGO_MEDIA_URL``
      - | URL that handles the media served
        | from ``MEDIA_ROOT``.
    * - ``SITE_ID``
      - ``1``
      - ``DJANGO_SITE_ID``
      - | The ID, as an integer, of the
        | current site in the
        | ``django_site`` database table.
    * - ``STATIC_ROOT``
      - ``'<full path to {{ cookiecutter.pkg_name }}>/static_root/'``
      - ``DJANGO_STATIC_ROOT``
      - | The absolute path to the directory
        | where :command:`collectstatic` will collect
        | static files for deployment. Must
        | be set for production sites.
    * - ``STATIC_URL``
      - ``'/static/'``
      - ``DJANGO_STATIC_URL``
      - | URL to use when referring to
        | static files located in
        | ``STATIC_ROOT``.
    * - ``STATICFILES_FINDERS``
      - | ``['django.contrib.staticfiles.finders.AppDirectoriesFinder',``
        | ``'django.contrib.staticfiles.finders.FileSystemFinder',]``
      - ``DJANGO_STATICFILES_FINDERS``
      - | The list of finder backends that
        | know how to find static files in
        | various locations.
    * - ``TIME_ZONE``
      - ``'Europe/Berlin'``
      - ``DJANGO_TIME_ZONE``
      - | A string representing the time
        | zone for this installation. See
        | the `list of time zones <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.

Database
========

The database settings are in
:py:class:`{{ cookiecutter.pkg_name }}.config.settings.databases.Databases`.

The following classes inherit from it:

* :py:class:`{{ cookiecutter.pkg_name }}.config.settings.dev.Development`
* :py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Production`
* :py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Staging`
* :py:class:`{{ cookiecutter.pkg_name }}.config.settings.test.Testing`

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``DEFAULT_DATABASE_URL``
      - ``''``
      - ``DEFAULT_DATABASE_URL``
      - | Database URL for the default
        | database connection.
        | Example environment value:
        | ``postgres://dbuser:password@localhost/database``
    * - ``DEFAULT_CONN_MAX_AGE``
      - ``600``
      - ``DJANGO_DEFAULT_CONN_MAX_AGE``
      - | The lifetime of a database
        | connection, in seconds.

Development
===========

The default class for development is
:py:class:`{{ cookiecutter.pkg_name }}.config.settings.dev.Development`.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``CACHES``
      - | ``{``
        | ``'default': {``
        | ``'BACKEND': 'django.core.cache.backends.dummy.DummyCache',``
        | ``}``
        | ``}``
      - ``DJANGO_CACHES``
      - | A dictionary containing the
        | settings for all caches to be used
        | with Django.
    * - ``EMAIL_BACKEND``
      - ``'django.core.mail.backends.console.EmailBackend'``
      - ``DJANGO_EMAIL_BACKEND``
      - | The backend to use for sending
        | emails.

SMTP
====

Settings for sending email using
:djangodocs:`SMTP <topics/email/#smtp-backend>`. Inherit from
:py:class:`{{ cookiecutter.pkg_name }}.config.settings.email.SMTP`
to use these settings.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``EMAIL_HOST``
      - ``'localhost'``
      - ``DJANGO_EMAIL_HOST``
      - | The host to use for sending email.
    * - ``EMAIL_HOST_PASSWORD``
      - ``''``
      - ``DJANGO_EMAIL_HOST_PASSWORD``
      - | Password to use for SMTP server
        | authentication. Must be set for
        | production sites if email should
        | be sent via SMTP.
    * - ``EMAIL_HOST_USER``
      - ``'noreply@example.com'``
      - ``DJANGO_EMAIL_HOST_USER``
      - | Username to use for SMTP server
        | authentication.
    * - ``EMAIL_PORT``
      - ``465``
      - ``DJANGO_EMAIL_PORT``
      - | Port to use for SMTP.
    * - ``EMAIL_USE_SSL``
      - ``True``
      - ``DJANGO_EMAIL_USE_SSL``
      - | Whether to use an implicit TLS
        | (secure) connection when talking
        | to the SMTP server. In most email
        | documentation this type of TLS
        | connection is referred to as SSL.
        | Default port is ``465``.
    * - ``EMAIL_USE_TLS``
      - ``False``
      - ``DJANGO_EMAIL_USE_TLS``
      - | Whether to use a TLS (secure)
        | connection when talking to the SMTP
        | server. Default port is ``587``.

Mailgun
=======

Settings for sending email using `Mailgun <https://www.mailgun.com/>`_. Inherit
from :py:class:`{{ cookiecutter.pkg_name }}.config.settings.email.Mailgun`
to use these settings.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``MAILGUN_ACCESS_KEY``
      - ``''``
      - ``DJANGO_MAILGUN_ACCESS_KEY``
      - | The secret Mailgun API key. You
        | can find it on the `Mailgun dashboard <https://mailgun.com/app/dashboard>`_.
    * - ``MAILGUN_SERVER_NAME``
      - ``'mg.transcode.de'``
      - ``DJANGO_MAILGUN_SERVER_NAME``
      - | Specifies the subdomain that is
        | being used for Mailgun. More
        | information on how to configure
        | your DNS records is available in
        | the `Mailgun User Manual <https://documentation.mailgun.com/user_manual.html#verifying-your-domain>`_.

Sentry
======

Settings to track errors using `Sentry <https://getsentry.com/>`_. Inherit
from :py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Raven`
to use these settings.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``RAVEN_CONFIG_DSN``
      - ``''``
      - ``DJANGO_RAVEN_CONFIG_DSN``
      - | `Sentry <https://getsentry.com/>`_ DSN, see
        | `Raven documentation <http://raven.readthedocs.org/en/latest/integrations/django.html>`_.
        | Must be set for production sites
        | to use Sentry.

Public
======

The class
:py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Public`
is the base class for the following classes:

* :py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Production`
* :py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Staging`

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``SECRET_KEY``
      - ``''``
      - ``DJANGO_SECRET_KEY``
      - | A secret key for a particular
        | Django installation, used to
        | provide cryptographic signing.
        | Must be set for public sites.
    * - ``SILENCED_SYSTEM_CHECKS``
      - ``[]``
      - ``DJANGO_SILENCED_SYSTEM_CHECKS``
      - | A list of identifiers of messages
        | generated by the system check
        | framework (i.e. ``["models.W001"]``)
        | that should be permanently
        | acknowledged and ignored.
        | See `list of builtin checks <https://docs.djangoproject.com/en/1.8/ref/checks/#builtin-checks>`_
        | Example environment value:
        | ``security.W004,security.W008``

SSL
===

Default settings for SSL-enabled servers. Inherit
from :py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.SSL`
to use these settings.
:py:class:`{{ cookiecutter.pkg_name }}.config.settings.public.Production`
inherits from this class by default. Make sure you read
:djangodocs:`Django's SSL <topics/security/#ssl-https>` documentation before
using these settings.

.. list-table::
    :header-rows: 1

    * - Setting
      - Default
      - Env Variable
      - Description
    * - ``CSRF_COOKIE_SECURE``
      - ``True``
      - ``DJANGO_CSRF_COOKIE_SECURE``
      - | If this is set to ``True``, the
        | cookie will be marked as “secure”,
        | which means browsers may ensure
        | that the cookie is only sent with
        | an HTTPS connection.
    * - ``SECURE_HSTS_INCLUDE_SUBDOMAINS``
      - ``True``
      - ``DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS``
      - | If ``True``, the
        | ``SecurityMiddleware`` adds the
        | ``includeSubDomains`` tag to the
        | HTTP Strict Transport Security
        | header.
    * - ``SECURE_HSTS_SECONDS``
      - ``3600``
      - ``DJANGO_SECURE_HSTS_SECONDS``
      - | If set to a non-zero integer
        | value, the ``SecurityMiddleware``
        | sets the HTTP Strict Transport
        | Security header on all responses
        | that do not already have it.
    * - ``SECURE_PROXY_SSL_HEADER``
      - ``None``
      - ``DJANGO_SECURE_PROXY_SSL_HEADER``
      - | A tuple representing a HTTP
        | header/value combination that
        | signifies a request is secure.
    * - ``SECURE_REDIRECT_EXEMPT``
      - ``[]``
      - ``DJANGO_SECURE_REDIRECT_EXEMPT``
      - | If a URL path matches a regular
        | expression in this list, the
        | request will not be redirected to
        | HTTPS.
    * - ``SECURE_SSL_HOST``
      - ``'{{ cookiecutter.domain }}'``
      - ``DJANGO_SECURE_SSL_HOST``
      - | If a string, all SSL redirects
        | will be directed to this host
        | rather than the
        | originally-requested host.
    * - ``SECURE_SSL_REDIRECT``
      - ``True``
      - ``DJANGO_SECURE_SSL_REDIRECT``
      - | If ``True``, the
        | ``SecurityMiddleware`` redirects
        | all non-HTTPS requests to HTTPS.
    * - ``SESSION_COOKIE_SECURE``
      - ``True``
      - ``DJANGO_SESSION_COOKIE_SECURE``
      - | If this is set to ``True``, the
        | cookie will be marked as “secure”,
        | which means browsers may ensure
        | that the cookie is only sent with
        | an HTTPS connection.
