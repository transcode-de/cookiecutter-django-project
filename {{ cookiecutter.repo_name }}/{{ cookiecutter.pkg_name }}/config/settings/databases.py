import dj_database_url
from configurations import values


class PostgreSQLDatabases(object):
    """Settings for local PostgreSQL databases."""

    DATABASES = {
        'default': dj_database_url.config(
            default='postgres://{{ cookiecutter.repo_name }}:{{ cookiecutter.repo_name }}@localhost/{{ cookiecutter.repo_name }}',  # noqa
            env='DEFAULT_DATABASE_URL'
        )
    }
    # Number of seconds database connections should persist for
    DATABASES['default']['CONN_MAX_AGE'] = values.IntegerValue(600, environ_prefix='',
        environ_name='DEFAULT_CONN_MAX_AGE')


class EmptyDatabases(object):
    """Empty databases settings, used to force to overwrite them."""

    DATABASES = {
        'default': dj_database_url.config(env='DEFAULT_DATABASE_URL')
    }
    # Number of seconds database connections should persist for
    DATABASES['default']['CONN_MAX_AGE'] = values.IntegerValue(600, environ_prefix='',
        environ_name='DEFAULT_CONN_MAX_AGE')
