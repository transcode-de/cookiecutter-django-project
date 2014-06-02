from .common import Public
from .databases import EmptyDatabases


class Stage(EmptyDatabases, Public):
    """Settings for staging server."""
    pass
