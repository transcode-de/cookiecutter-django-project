from configurations import values

from . import common, databases, email
from .. import __version__


class Raven(object):
    """Report uncaught exceptions to the Sentry server."""

    INSTALLED_APPS = common.Common.INSTALLED_APPS + ('raven.contrib.django.raven_compat',)

    RAVEN_CONFIG = {
        'dsn': values.URLValue(environ_name='RAVEN_CONFIG_DSN'),
        'release': __version__,
    }


class Sentry404(Raven):
    """Log 404 events to the Sentry server."""

    MIDDLEWARE_CLASSES = (
        'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    ) + common.Common.MIDDLEWARE_CLASSES


class Public(email.Email, databases.Databases, common.Common):
    """General settings for public projects."""

    SECRET_KEY = values.SecretValue()

    CSRF_COOKIE_HTTPONLY = True

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = 'DENY'

    SILENCED_SYSTEM_CHECKS = values.ListValue([])


class Stage(Public):
    """Settings for staging server."""

    pass


class SSL(object):
    """Settings for SSL."""

    SECURE_SSL_HOST = values.Value('{{ cookiecutter.domain }}')

    SECURE_SSL_REDIRECT = True


class Prod(Public, SSL):
    """Settings for production server."""

    pass
