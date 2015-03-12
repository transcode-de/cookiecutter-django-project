#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from codecs import open

from setuptools import find_packages, setup


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django==1.7.6',
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

docs_requires = [
    'Sphinx==1.2.2',
]

tests_requires = [
    'coverage==3.7.1',
    'factory_boy==2.4.1',
    'freezegun==0.2.8',
    'isort==3.9.4',
    'pytest-django==2.7.0',
    'pytest==2.6.4',
    'tox==1.9.0',
]

setup(
    name='{{ cookiecutter.pkg_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    long_description=read('README.rst'),
    author='transcode',
    author_email='{{ cookiecutter.email }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'docs': docs_requires,
        'tests': tests_requires,
    },
    license='{{ cookiecutter.license }}',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        {% if cookiecutter.license|lower == 'bsd' -%}
        'License :: OSI Approved :: BSD License',
        {%- endif %}
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
