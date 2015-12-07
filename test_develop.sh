#!/bin/bash
export PYTHONIOENCODING=UTF-8
cd my-project

# Set up the development environment
make develop
PG_UUID=`faker uuid4`
if [ "$CI" = true ] ; then
    PG_CREATE_USER="-U postgres"
else
    PG_CREATE_USER=
fi
createuser -d -e $PG_UUID $PG_CREATE_USER
echo $PG_UUID > envs/dev/PGPASSWORD
echo "postgres://$PG_UUID:$PG_UUID@localhost/$PG_UUID" > envs/dev/DEFAULT_DATABASE_URL

# Run the tests and collect coverage data
cat >> tests/test_context_processors.py <<EOF

import pytest


@pytest.mark.django_db
def test_db(admin_user):
    assert admin_user.is_superuser
EOF
make coverage

# Clean up
dropuser -e $PG_UUID
