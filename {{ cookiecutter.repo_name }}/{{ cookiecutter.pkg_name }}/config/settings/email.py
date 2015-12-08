from configurations import values


class Email(object):
    """Email settings for SMTP."""

    EMAIL_HOST = values.Value('localhost')
    EMAIL_PORT = values.IntegerValue(465)
    EMAIL_USE_TLS = values.BooleanValue(False)
    EMAIL_USE_SSL = values.BooleanValue(True)
    EMAIL_HOST_USER = values.Value('{{ cookiecutter.email }}')
    EMAIL_HOST_PASSWORD = values.SecretValue()


class Mailgun(object):
    """Email settings for Mailgun."""

    EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
    MAILGUN_ACCESS_KEY = values.SecretValue()
    MAILGUN_SERVER_NAME = values.Value('mg.transcode.de')
