import socket

from configurations import values

from .common import Common
from .databases import PostgreSQLDatabases


class Dev(PostgreSQLDatabases, Common):
    """Settings for development."""
    def get_addr(self):
        if socket.gethostname() == 'vagrant':
            addr = socket.gethostbyname(socket.gethostname())
        else:
            addr = '127.0.0.1'
        return addr

    @property
    def INTERNAL_IPS(self):
        return (self.get_addr(),)

    # devserver must be ahead of django.contrib.staticfiles
    INSTALLED_APPS = ('devserver',) + Common.INSTALLED_APPS + ('debug_toolbar',)

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    @property
    def DEVSERVER_DEFAULT_ADDR(self):
        return self.get_addr()

    DEVSERVER_ARGS = values.ListValue([])

    DEVSERVER_TRUNCATE_SQL = values.BooleanValue(True)

    DEVSERVER_MODULES = (
        'devserver.modules.sql.SQLRealTimeModule',
        'devserver.modules.sql.SQLSummaryModule',
        'devserver.modules.profile.ProfileSummaryModule',
    )

    # Beware before activating this! Grappelli has problems with admin
    # inlines and TEMPLATE_STRING_IF_INVALID.
    TEMPLATE_STRING_IF_INVALID = values.Value('')
