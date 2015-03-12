from .common import Public
from .databases import EmptyDatabases


class Prod(EmptyDatabases, Public):
    """Settings for production server."""
    pass
