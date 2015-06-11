import os

from configurations import Configuration, values


class BaseDir(object):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Email(object):
    """Email settings for public projects."""
    EMAIL_HOST = values.Value('localhost')
    EMAIL_PORT = values.IntegerValue(25)  # Alternate TLS port is 587
    EMAIL_USE_TLS = values.BooleanValue(True)
    EMAIL_HOST_USER = values.Value('{{ cookiecutter.email }}')
    EMAIL_HOST_PASSWORD = values.SecretValue()


class Common(Configuration):
    SECRET_KEY = '(_j4e0=pbe(b+b1$^ch_48be0=gszglcgfzz^dy=(gnx=@m*b7'

    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ADMINS = (
        ('transcode', 'traceback@transcode.de'),
    )
    MANAGERS = ADMINS

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            },
            'null': {
                'class': 'logging.NullHandler',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.security.DisallowedHost': {
                'handlers': ['null'],
                'propagate': False,
            },
            'py.warnings': {
                'handlers': ['console'],
            },
        }
    }

    ALLOWED_HOSTS = values.ListValue([])

    SITE_ID = 1

    # Internationalization
    # https://docs.djangoproject.com/en/dev/topics/i18n/
    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('Europe/Berlin')

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"
    MEDIA_ROOT = os.path.join(BaseDir.BASE_DIR, 'media')

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = '/media/'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/var/www/example.com/static/"
    STATIC_ROOT = os.path.join(BaseDir.BASE_DIR, 'static_root')

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/dev/howto/static-files/
    STATIC_URL = '/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(BaseDir.BASE_DIR, 'static'),
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'config.urls'

    WSGI_APPLICATION = 'config.wsgi.application'

    TEMPLATE_DIRS = (
        os.path.join(BaseDir.BASE_DIR, 'templates'),
    )

    FIXTURE_DIRS = (
        os.path.join(BaseDir.BASE_DIR, 'fixtures'),
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'grappelli',  # grappelli must be listed before django.contrib.admin!
        'django.contrib.admin',
        'django.contrib.admindocs',
        'crispy_forms',
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'config.context_processors.django_version',
    )

    CRISPY_TEMPLATE_PACK = 'bootstrap3'

    GRAPPELLI_ADMIN_TITLE = '{{ cookiecutter.project_name }} Admin'

    EMAIL_SUBJECT_PREFIX = '[{{ cookiecutter.project_name }}]'
    DEFAULT_FROM_EMAIL = '{{ cookiecutter.email }}'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL


class Public(Email, Common):
    """Settings for public projects."""
    SECRET_KEY = values.SecretValue()
