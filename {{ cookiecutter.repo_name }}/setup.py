#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open
import os
from sys import platform

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django==1.7.4',
    'dj-database-url==0.3.0',
    'django-braces==1.4.0',
    'django-configurations==0.8',
    'django-crispy-forms==1.4.0',
    'django-grappelli==2.6.3',
    'envdir==0.7',
    'psycopg2==2.5.4',
    'pytz==2014.10',
    'six==1.9.0',
    'wheel==0.24.0',
]

dev_requires = [
    'Werkzeug==0.9.6',
    'bumpversion==0.5.1',
    'django-debug-toolbar==1.2.2',
    # This version should be used with Django>=1.7
    'https://github.com/nealtodd/django-devserver/archive/master.zip',
    'ipdb==0.8',
    'ipython==2.3.1',
    'sqlparse==0.1.14',
]

if platform == 'darwin':
    dev_requires.append('gnureadline==6.3.3')

docs_requires = [
    'Sphinx==1.2.2',
]

tests_requires = [
    'factory_boy==2.4.1',
    'freezegun==0.2.8',
    'isort==3.9.4',
    'pytest-cov==1.8.1',
    'pytest-django==2.7.0',
    'pytest-flakes==0.2',
    'pytest-pep8==1.0.6',
    'pytest==2.6.4',
    'tox==1.9.0',
]

setup(
    name={{ cookiecutter.repo_name }},
    version={{ cookiecutter.version }},
    description={{ cookiecutter.description }},
    long_description=read('README.rst'),
    author='transcode',
    author_email='team@transcode.de',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
        'docs': docs_requires,
        'tests': tests_requires,
    },
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
