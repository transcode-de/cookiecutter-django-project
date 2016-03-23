import socket
import subprocess

from configurations import values

from . import common, databases


class Development(databases.Databases, common.Common):
    """Settings for development."""

    CACHES = values. DictValue({
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    })

    DEVSERVER_ARGS = values.ListValue([])

    @property
    def DEVSERVER_DEFAULT_ADDR(self):  # noqa
        """Return the default address to bind devserver to."""
        if 'vagrant' in socket.gethostname():
            addr = '0.0.0.0'
        else:
            addr = '127.0.0.1'
        return addr

    DEVSERVER_MODULES = values.ListValue([
        'devserver.modules.sql.SQLRealTimeModule',
        'devserver.modules.sql.SQLSummaryModule',
        'devserver.modules.profile.ProfileSummaryModule',
    ])

    DEVSERVER_TRUNCATE_SQL = values.BooleanValue(True)

    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')

    # devserver must be ahead of django.contrib.staticfiles
    INSTALLED_APPS = ('devserver',) + common.Common.INSTALLED_APPS + ('debug_toolbar',)

    @property
    def INTERNAL_IPS(self):  # noqa
        """Return a tuple of IP addresses, as strings.

        Detect a Vagrant box by looking at the hostname. Return the gateway IP
        address on a Vagrant box, because this is the IP address the request
        will originate from.
        """
        if 'vagrant' in socket.gethostname():
            addr = [line.split()[1] for line in subprocess.check_output(['netstat', '-rn']).splitlines() if line.startswith('0.0.0.0')][0]  # noqa
        else:
            addr = '127.0.0.1'
        return (addr,)
