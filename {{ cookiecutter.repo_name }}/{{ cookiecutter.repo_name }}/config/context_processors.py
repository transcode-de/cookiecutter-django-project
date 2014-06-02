import django


def django_version(request):
    """Adds the Django version to the context."""
    return {'django_version': django.get_version()}
