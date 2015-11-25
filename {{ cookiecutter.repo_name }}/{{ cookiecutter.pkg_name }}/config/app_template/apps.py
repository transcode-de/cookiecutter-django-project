from django.apps import AppConfig


class {{ '{{ app_name|title }}' }}Config(AppConfig):
    name = '{{ cookiecutter.pkg_name }}.apps.{{ '{{ app_name }}' }}'
