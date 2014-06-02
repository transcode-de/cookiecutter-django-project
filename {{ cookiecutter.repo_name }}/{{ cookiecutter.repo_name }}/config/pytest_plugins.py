# encoding: utf-8
from functools import partial

import pytest


@pytest.fixture
def loaddata(settings, transactional_db):
    """Loads a Django fixture.

    Works exactly like the loaddata command. All command line options
    must be given as keyword arguments.

    There is no no need to mark the test itself with the django_db
    marker because the loaddata fixture has already started a database
    transaction.

    This fixture enables timezone support by default.

    Usage::

        def test_model(loaddata):
            loaddata('my_fixture')
            # do a test using the fixture


        def test_othermodel(loaddata):
            loaddata('other_fixture', database='other')
            # do a test using the fixture
    """
    settings.USE_TZ = True
    from django.core import management
    return partial(management.call_command, 'loaddata')
