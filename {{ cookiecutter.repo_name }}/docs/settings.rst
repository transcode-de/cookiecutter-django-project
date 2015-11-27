********
Settings
********

This is a list of all settings for this project. Each setting can be configured
using environment variables.

.. Keep the length of the "Description" column at a maximum of 45 characters.

.. list-table::
    :header-rows: 1

    * - App/Package
      - Setting
      - Default
      - Env Variable
      - Description
    * - ``configurations``
      - ``DJANGO_CONFIGURATION``
      - ``'Dev'``
      - ``DJANGO_CONFIGURATION``
      - | Name of the django-configurations
        | class you want to use.
    * - ``configurations``
      - ``DJANGO_SETTINGS_MODULE``
      - ``'{{ cookiecutter.pkg_name }}.config.settings.dev'``
      - ``DJANGO_SETTINGS_MODULE``
      - | Python path to the settings module
        | for this project.
    * - ``devserver``
      - ``DEVSERVER_ARGS``
      - ``[]``
      - ``DJANGO_DEVSERVER_ARGS``
      - | Additional command line
        | arguments to pass to the :command:`runserver`
        | command (as defaults).
        | Example environment value: ``--werkzeug``
    * - ``devserver``
      - ``DEVSERVER_MODULES``
      - | ``('devserver.modules.sql.SQLRealTimeModule',``
        | ``'devserver.modules.sql.SQLSummaryModule',``
        | ``'devserver.modules.profile.ProfileSummaryModule',)``
      - ``DJANGO_DEVSERVER_MODULES``
      - | django-devserver modules. See
        | `list of available modules <https://github.com/dcramer/django-devserver>`_.
    * - ``devserver``
      - ``DEVSERVER_TRUNCATE_SQL``
      - ``True``
      - ``DJANGO_DEVSERVER_TRUNCATE_SQL``
      - | Enables SQL query truncation
        | (used in ``SQLRealTimeModule``).
    * - ``dj_database_url``
      - ``DEFAULT_DATABASE_URL``
      - ``''``
      - ``DEFAULT_DATABASE_URL``
      - | Database URL for the default
        | database connection.
        | Example environment value: ``postgres://dbuser:password@localhost/database``
    * - ``django.core.mail.backends.smtp.EmailBackend``
      - ``EMAIL_HOST``
      - ``'localhost'``
      - ``DJANGO_EMAIL_HOST``
      - | The host to use for sending email.
    * - ``django.core.mail.backends.smtp.EmailBackend``
      - ``EMAIL_PORT``
      - ``465``
      - ``DJANGO_EMAIL_PORT``
      - | Port to use for SMTP.
    * - ``django.core.mail.backends.smtp.EmailBackend``
      - ``EMAIL_USE_TLS``
      - ``False``
      - ``DJANGO_EMAIL_USE_TLS``
      - | Whether to use a TLS (secure)
        | connection when talking to the SMTP
        | server. Default port is ``587``.
    * - ``django.core.mail.backends.smtp.EmailBackend``
      - ``EMAIL_USE_SSL``
      - ``True``
      - ``DJANGO_EMAIL_USE_TLS``
      - | Whether to use an implicit TLS
        | (secure) connection when talking
        | to the SMTP server. In most email
        | documentation this type of TLS
        | connection is referred to as SSL.
        | Default port is ``465``.
    * - ``django.core.mail.backends.smtp.EmailBackend``
      - ``EMAIL_HOST_USER``
      - ``'noreply@example.com'``
      - ``DJANGO_EMAIL_HOST_USER``
      - | Username to use for SMTP server
        | authentication.
    * - ``django.core.mail.backends.smtp.EmailBackend``
      - ``EMAIL_HOST_PASSWORD``
      - ``''``
      - ``DJANGO_EMAIL_HOST_PASSWORD``
      - | Password to use for SMTP server
        | authentication. Must be set for
        | production sites if email should
        | be sent via SMTP.
    * - ``django.conf.settings``
      - ``ADMINS``
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
    * - ``django.conf.settings``
      - ``ALLOWED_HOSTS``
      - ``[]``
      - ``DJANGO_ALLOWED_HOSTS``
      - | A list of strings representing the
        | host/domain names that this Django
        | site can serve.
        | Example environment value:
        | ``example.com,www.example.com``
    * - ``django.conf.settings``
      - ``DEBUG``
      - ``False``
      - ``DJANGO_DEBUG``
      - | A boolean that turns on/off debug
        | mode. Never deploy a site into
        | production with ``DEBUG`` turned
        | on.
    * - ``django.conf.settings``
      - ``DEFAULT_FROM_EMAIL``
      - ``'noreply@example.com'``
      - ``DJANGO_DEFAULT_FROM_EMAIL``
      - | Default email address to use for
        | various automated correspondence.
    * - ``django.conf.settings``
      - ``MEDIA_ROOT``
      - ``'{{ cookiecutter.pkg_name }}/media/'``
      - ``DJANGO_MEDIA_ROOT``
      - | Absolute filesystem path to the
        | directory that will hold
        | user-uploaded files. Must be
        | changed for production sites.
    * - ``django.conf.settings``
      - ``SECRET_KEY``
      - ``''``
      - ``DJANGO_SECRET_KEY``
      - | A secret key for a particular
        | Django installation, used to
        | provide cryptographic signing.
        | Must be set for production sites.
    * - ``django.conf.settings``
      - ``SILENCED_SYSTEM_CHECKS``
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
    * - ``django.conf.settings``
      - ``STATIC_ROOT``
      - ``'{{ cookiecutter.pkg_name }}/static_root/'``
      - ``DJANGO_STATIC_ROOT``
      - | The absolute path to the directory
        | where :command:`collectstatic` will collect
        | static files for deployment. Must
        | be set for production sites.
    * - ``django.conf.settings``
      - ``TIME_ZONE``
      - ``'Europe/Berlin'``
      - ``DJANGO_TIME_ZONE``
      - | A string representing the time
        | zone for this installation. See
        | the `list of time zones <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.
    * - ``django_mailgun.MailgunBackend``
      - ``MAILGUN_ACCESS_KEY``
      - ``''``
      - ``DJANGO_MAILGUN_ACCESS_KEY``
      - | The secret Mailgun API key. You
        | can find it on the `Mailgun dashboard <https://mailgun.com/app/dashboard>`_.
    * - ``django_mailgun.MailgunBackend``
      - ``MAILGUN_SERVER_NAME``
      - ``'mg.transcode.de'``
      - ``DJANGO_MAILGUN_SERVER_NAME``
      - | Specifies the subdomain that is
        | being used for Mailgun. More
        | information on how to configure
        | your DNS records is available in
        | the `Mailgun User Manual <https://documentation.mailgun.com/user_manual.html#verifying-your-domain>`_.
    * - ``raven``
      - ``RAVEN_CONFIG_DSN``
      - ``''``
      - ``DJANGO_RAVEN_CONFIG_DSN``
      - | `Sentry <https://getsentry.com/>`_ DSN, see
        | `Raven documentation <http://raven.readthedocs.org/en/latest/integrations/django.html>`_.
        | Must be set for production sites
        | to use Sentry.


All further setting variables that are configurable can be found in
:file:`{{ cookiecutter.pkg_name }}/config/settings/common.py`.
