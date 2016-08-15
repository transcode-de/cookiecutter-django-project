from . import common, databases


class Testing(databases.Databases, common.Common):
    """Settings for running the test suite."""

    # Use a fast hasher to speed up tests.
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
