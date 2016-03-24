************
Installation
************

Prerequisites
=============

pip and setuptools
------------------

Make sure you have the latest versions of `pip
<https://pip.pypa.io/en/stable/>`_ and `setuptools
<https://bitbucket.org/pypa/setuptools>`_  installed.

::

    $ pip --version

.. note::

    The package managers of most Linux/Unix distributions usually use outdated
    versions of :program:`pip`. Please uninstall the package providing
    :program:`pip` (usually it's named ``python-pip``) and :ref:`reinstall it
    using the bootstrap script <pip_bootstrap_script>`.

Install/upgrade pip using ensurepip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have Python 3.4 (or newer) or Python 2.7.9 (or newer) installed you can
use `ensurepip <https://docs.python.org/3/library/ensurepip.html>`_ to install
or upgrade :program:`pip`:

::

    $ python -m ensurepip --upgrade

If your Python version is too old you will simply see an error message like
that:

::

    $ python -m ensurepip --upgrade
    /usr/bin/python: No module named ensurepip

In this case :ref:`reinstall it using the bootstrap script
<pip_bootstrap_script>`.

.. _pip_bootstrap_script:

Install/upgrade pip using the bootstrap script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:program:`pip` can be installed with the help from a `bootstrap script
<https://bootstrap.pypa.io/get-pip.py>`_. If :program:`curl` is installed, you
can use it to download :program:`pip` at the command line. Otherwise just use
the browser.

::

    $ curl -O https://bootstrap.pypa.io/get-pip.py

When the bootstrap script has been downloaded execute it to install
:program:`pip`:

::

    $ python get-pip.py

virtualenvwrapper
-----------------

Make sure you have installed the latest version of `virtualenvwrapper
<https://virtualenvwrapper.readthedocs.org/>`_. You can use :program:`pip` to
either install or upgrade it:

::

    $ pip install -U virtualenvwrapper

.. note::

    If you installed :program:`virtualenvwrapper` for the first time, take your
    time to read the installation documentation.

pyenv
-----

This project will be tested with different Python versions. You should install
`pyenv <https://github.com/yyuu/pyenv>`_ to make the installation of different
Python versions as easy as possible.

Also install `pyenv-virtualenvwrapper <https://github.com/yyuu/pyenv-
virtualenvwrapper>`_, a :program:`pyenv` plugin which provides a
:program:`pyenv virtualenvwrapper` command to manage your virtualenvs with
virtualenvwrapper.

After you have installed and configured :program:`pyenv` and the plugin you can
use the following command in the root of the project to configure the Python
versions to use:

::

    $ pyenv local 3.4.3 2.7.9

.. note::

    You first have to install the Python versions you want to use using
    :program:`pyenv install`. :program:`pyenv install -l` lists all available
    versions.

    The first version passed to :program:`pyenv local` will be the main version
    used for the project.

Node.js and npm
---------------

`Node.js <https://nodejs.org/>`_ is an asynchronous event driven framework,
similar in design to and influenced by systems like Ruby's Event Machine or
Python's Twisted. The `npm <https://www.npmjs.com/>`_ package manager is
bundled with Node.js. Both will be used to install packages and take care of
tasks for the frontend.

Visit the `Node.js download page <https://nodejs.org/en/download/package-manager/>`_
to figure out how to install both.

PostgreSQL
----------

Check if PostgreSQL is installed:

::

    $ psql --version

If not, `download <http://www.postgresql.org/download/>`_ and install it for
your operating system.

EditorConfig
------------

`EditorConfig <http://editorconfig.org/>`_ helps developers define and maintain
consistent coding styles between different editors and IDEs. `Download a plugin
<http://editorconfig.org/#download>`_ for your favourite editor to enable it to
read the file format and adhere to the defined styles.

Development Setup
=================

Git and git-flow
----------------

Clone the repository using `Git <https://git-scm.com/>`_:

::

    $ git clone git@github.com:{{ cookiecutter.github_account }}/{{ cookiecutter.repo_name }}.git

Then change into the cloned repository:

::

    $ cd {{ cookiecutter.repo_name }}

We are using `git-flow <https://github.com/nvie/gitflow/>`_, a set of git
extensions for a branching model introduced by Vincent Driessen. You can read
more about it on `Vincent's blog
<http://nvie.com/posts/a-successful-git-branching-model/>`_, where you can also
find a `high-quality PDF illustrating the model
<http://nvie.com/files/Git-branching-model.pdf>`_. For your daily workflow
there also the `git-flow cheatsheet
<https://danielkummer.github.io/git-flow-cheatsheet/>`_ created by Daniel
Kummer, which is very helpful.

If you havn't installed git-flow, `do it now
<https://danielkummer.github.io/git-flow-cheatsheet/#setup>`_!

So the next step is to initialize your repository clone with git-flow. You can
choose the default for all questions being asked during the initialzaion
(simply press :kbd:`Enter` on every question):

::

    $ git-flow init

Install Python and JavaScript packages
--------------------------------------

First create a new virtualenv for the project using virtualenvwrapper:

::

    $ mkvirtualenv -a `pwd` {{ cookiecutter.repo_name }}

Now you can install the packages for development:

::

    $ make develop

You should run this command every time a requirement changes to update your
development environment. It will install or update all required Python and
JavaScript packages.

Create the database
-------------------

Then create the new PostgreSQL user and database:

::

    $ make create-db-user
    $ make create-db

.. note::

    You may need to run :command:`make create-db-user` as a PostgreSQL superuser:

    ::

        $ sudo -u postgres make create-db-user

.. note::

    You may have to edit the PostgreSQL permissions in :file:`pg_hba.conf` by
    adding a line as follows after the ``postgres`` user line:

    ::

        local      {{ cookiecutter.repo_name }}   {{ cookiecutter.repo_name }}   md5

Now it's the time to create the database tables:

::

    $ make migrate

And to create a new Django superuser:

::

    $ envdir envs/dev/ python manage.py createsuperuser

Start the development webserver
-------------------------------

Finally start Django's development webserver:

::

    $ make runserver

But this way `webpack <https://webpack.github.io/>`_ won't be started to build
the JavaScript and CSS bundle. So use
`Honcho <https://github.com/nickstenning/honcho>`_ to start both, runserver and
webpack:

::

    $ honcho start

Now open http://localhost:3000/ in your Browser. This is Django's development
webserver, but it's proxied through `Browsersync
<https://www.browsersync.io/>`_. If you open the URL in different browsers,
Browsersync will synchronize them. If you click in one browser, the others will
automatically do the same. It also watches all JavaScript, SASS and Python
files. If any of these files is changed, Browsersync reloads all synchronized
browsers. If you open http://localhost:3001/ you will see Browsersync's UI. You
can use it to configure it, for example you can set a network throttle to
emulate slow connections.

If you don't want to use Honcho you can also start Django's development
webserver and webpack with Browsersync manually. Of course you will need two
terminals for that. In the first terminal start Django's development webserver:

    $ make runserver

To see the other targets available in the :file:`Makefile` simply run:

::

    $ make
