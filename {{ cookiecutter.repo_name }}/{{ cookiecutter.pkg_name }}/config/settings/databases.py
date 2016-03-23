import dj_database_url
from configurations import values


class Databases(object):
    """Settings for PostgreSQL databases."""

    DATABASES = {
        'default': dj_database_url.config(env='DEFAULT_DATABASE_URL')
    }

    # Number of seconds database connections should persist for
    DATABASES['default']['CONN_MAX_AGE'] = values.IntegerValue(
        600,
        environ_prefix='',
        environ_name='DEFAULT_CONN_MAX_AGE'
    )
