import django


def django_version(request):
    """Add the Django version to the context."""
    return {'django_version': django.get_version()}
