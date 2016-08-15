"""
WSGI config for {{ cookiecutter.repo_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.pkg_name }}.config.settings.dev')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
