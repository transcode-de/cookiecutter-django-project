********
Releases
********

Since `git-flow <https://github.com/nvie/gitflow/>`_ is used to organize the
work in feature branches it will also be used to create the releases. Before
you start a new release make sure all feature branches you want to be part of
the release have been merged into the ``develop`` branch.

Furthermore it's assumed that `protected branches
<https://help.github.com/articles/configuring-protected-branches/>`_ and
`required status checks
<https://help.github.com/articles/enabling-required-status-checks/>`_ are
enabled on GitHub. Usually the branches ``develop`` and ``master`` are
configured as protected branches and status checks for continuous integration
and code coverage are required.

Start a new release branch
==========================

Let's assume all features for the next release are merged into the ``develop``
branch and the next release should be version ``1.0.0``.

So the first step is to start a new release branch:

::

    $ git flow release start 1.0.0

After that you will be on the newly created ``release/1.0.0`` branch.

Prepare the release branch
==========================

The next thing to do is to update the version numbers using
`bumpversion <https://github.com/peritus/bumpversion>`_. Since this is a new
major release we need to pass the ``major`` keyword to :program:`bumpversion`.
Other possible keyword for the version number part are ``patch`` for bugfix
releases (example: ``0.8.2``) and ``minor`` for minor releases (example
``0.9.0``).

::

    $ bumpversion major

Now run the test suite to make sure everything works as expected:

::

    $ make clean test-all

Fix any errors or failures that occur directly in the release branch.

Publish the release branch
==========================

Then push the new branch ``release/1.0.0`` to the GitHub remote to run the
required status checks for the release branch:

::

    $ git push --set-upstream origin release/1.0.0

Finish the release branch
=========================

After all GitHub status checks have passed you can finish the release branch:

::

    $ git flow release finish 1.0.0

Now you change to the ``master`` branch and push it together with the new tag
``1.0.0`` to the GitHub remote:

::

    $ git checkout master
    $ git push origin master
    $ git push origin master --tags

Create an integration branch to merge ``master`` into ``develop``
=================================================================

Then checkout the ``develop`` branch:

::

    $ git checkout develop

You will recognize that it has already been merged with ``master``. But for a
protected branches configuration where ``master`` and ``develop`` are protected
this does not work.

So create a new integration branch to merge ``master`` into ``develop``:

::

    $ git checkout -b merge-master-into-develop-for-release-1.0.0

After that fetch the latest changes, merge with the integration branch and push
it:

::

    $ git fetch
    $ git merge origin/develop
    $ git push --set-upstream origin merge-master-into-develop-for-release-1.0.0

Now that we have the merge of ``master`` into ``develop`` in a separate
integration branch we can safely reset the ``develop`` branch:

::

    $ git checkout develop
    $ git reset --hard origin/develop

The last step create a new pull request for the integration branch
``merge-master-into-develop-for-release-1.0.0`` on GitHub, merge and delete it
after all required status checks have passed.

Clean up
========

Finally delete all stale remote-tracking branches for ``origin``, the local
branch ``merge-master-into-develop-for-release-1.0.0`` and the remote-tracking
branch ``release/1.0.0``:

::

    $ git pull
    $ git remote prune origin
    $ git branch -d merge-master-into-develop-for-release-1.0.0
    $ git push origin :release/1.0.0
