from django.conf import settings

"""Filter functions for python logging framework."""


def RequireMailAdminsTrue():
    """Return MAIL_ADMINS setting."""
    return settings.MAIL_ADMINS
