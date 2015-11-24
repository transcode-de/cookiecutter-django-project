import os

from configurations import Configuration, values
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class AdminsValue(values.SingleNestedTupleValue):
    """A ``SingleNestedTupleValue`` subclass to be used for the ADMINS and MANAGERS settings.

    Two validators are executed for each tuple:

        1. The exact length of each tuple must be two.
        2. The second element of each tuple must be a valid email address.
    """
    def __init__(self, *args, **kwargs):
        super(AdminsValue, self).__init__(*args, **kwargs)
        if self.default:
            self.validate(self.default)

    def validate_length(self, value):
        if len(value) != 2:
            raise ValueError('Each ADMINS tuple must have exact two values')

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise ValueError('Cannot interpret email value {0!r}'.format(value))

    def validate(self, value):
        for item in value:
            self.validate_length(item)
            self.validate_email(item[1])

    def to_python(self, value):
        value = super(AdminsValue, self).to_python(value)
        self.validate(value)
        return value


class BaseDir(object):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Email(object):
    """Default Email settings for public projects."""

    EMAIL_HOST = values.Value('localhost')
    EMAIL_PORT = values.IntegerValue(25)  # Alternate TLS port is 587
    EMAIL_USE_TLS = values.BooleanValue(True)
    EMAIL_HOST_USER = values.Value('{{ cookiecutter.email }}')
    EMAIL_HOST_PASSWORD = values.SecretValue()


class MailgunEmail(object):
    """Email settings for public projects using Mailgun."""

    EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
    MAILGUN_ACCESS_KEY = values.SecretValue()
    MAILGUN_SERVER_NAME = values.Value('mg.transcode.de')


class Common(Configuration):
    SECRET_KEY = '(_j4e0=pbe(b+b1$^ch_48be0=gszglcgfzz^dy=(gnx=@m*b7'

    DEBUG = values.BooleanValue(False)

    ADMINS = AdminsValue(
        (('{{ cookiecutter.author_name }}', '{{ cookiecutter.error_email }}'),)
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
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = '{{ cookiecutter.pkg_name }}.config.urls'

    WSGI_APPLICATION = '{{ cookiecutter.pkg_name }}.config.wsgi.application'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BaseDir.BASE_DIR, 'templates'), ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    '{{ cookiecutter.pkg_name }}.context_processors.django_version',
                ],
                # Beware before activating this! Grappelli has problems with admin
                # inlines and the template backend option 'string_if_invalid'.
                'string_if_invalid': values.Value('', environ_name='TEMPLATE_STRING_IF_INVALID'),
            },
        },
    ]

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

    CRISPY_TEMPLATE_PACK = 'bootstrap3'

    GRAPPELLI_ADMIN_TITLE = '{{ cookiecutter.project_name }} Admin'

    EMAIL_SUBJECT_PREFIX = '[{{ cookiecutter.project_name }}]'
    DEFAULT_FROM_EMAIL = '{{ cookiecutter.email }}'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL


class Public(Email, Common):
    """Settings for public projects."""
    SECRET_KEY = values.SecretValue()
