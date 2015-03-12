from configurations import values


class PostgreSQLDatabases(object):
    """Settings for local PostgreSQL databases."""
    DATABASES = values.DictValue({
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '{{ cookiecutter.repo_name }}',
            'USER': '{{ cookiecutter.repo_name }}',
            'PASSWORD': '{{ cookiecutter.repo_name }}',
            'HOST': 'localhost',
            'CONN_MAX_AGE': 600,
        },
    })


class EmptyDatabases(object):
    """Empty databases settings, used to force to overwrite them."""
    DATABASES = values.DictValue({
        'default': {
            'ENGINE': '',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
        },
    })
