# encoding: utf-8
from functools import partial

import pytest
from faker import Faker


@pytest.fixture
def loaddata(settings, db):
    """Load a Django fixture.

    Works exactly like the loaddata command. All command line options must be
    given as keyword arguments.

    There is no no need to mark the test itself with the django_db marker
    because the loaddata fixture already loads the db fixture.

    Usage::

        def test_model(loaddata):
            loaddata('my_fixture')
            # do a test using the fixture


        def test_othermodel(loaddata):
            loaddata('other_fixture', database='other')
            # do a test using the fixture
    """
    from django.core import management
    return partial(management.call_command, 'loaddata')


def pytest_runtest_setup(item):
    """Seed the Faker generator for every test.

    Faker is seeded at the beginning of each test based on the test name, so
    each test that uses Faker will use the same fake data between test runs,
    regardless of test order.

    Requires fake-factory 0.5.3 or newer.
    """
    Faker().seed(item.nodeid)
