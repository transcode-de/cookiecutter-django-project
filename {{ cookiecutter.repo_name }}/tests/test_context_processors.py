import django

from config import context_processors


def test_django_version():
    assert context_processors.django_version(None) == {'django_version': django.get_version()}
