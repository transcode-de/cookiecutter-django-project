from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class {{ '{{ app_name|title }}' }}Config(AppConfig):
    """Configuration for {{ '{{ app_name }}' }} app."""

    name = '{{ cookiecutter.pkg_name }}.apps.{{ '{{ app_name }}' }}'
    verbose_name = _("{{ '{{ app_name|title }}' }}")
