import socket
import subprocess

from configurations import values

from . import common, databases


class Dev(databases.Databases, common.Common):
    """Settings for development."""

    def get_client_ip(self):
        """Return the client IP address.

        Detect a Vagrant box by looking at the hostname. Return the gateway IP
        on a Vagrant box, because this is the IP the request will originate
        from.
        """
        if 'vagrant' in socket.gethostname():
            addr = [line.split()[1] for line in subprocess.check_output(['netstat', '-rn']).splitlines() if line.startswith('0.0.0.0')][0]  # noqa
        else:
            addr = '127.0.0.1'
        return addr

    @property
    def INTERNAL_IPS(self):
        """Return a tuple of IP addresses, as strings."""
        return (self.get_client_ip(),)

    # devserver must be ahead of django.contrib.staticfiles
    INSTALLED_APPS = ('devserver',) + common.Common.INSTALLED_APPS + ('debug_toolbar',)

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    @property
    def DEVSERVER_DEFAULT_ADDR(self):
        """Return the default address to bind devserver to."""
        return self.get_client_ip()

    DEVSERVER_ARGS = values.ListValue([])

    DEVSERVER_TRUNCATE_SQL = values.BooleanValue(True)

    DEVSERVER_MODULES = (
        'devserver.modules.sql.SQLRealTimeModule',
        'devserver.modules.sql.SQLSummaryModule',
        'devserver.modules.profile.ProfileSummaryModule',
    )
