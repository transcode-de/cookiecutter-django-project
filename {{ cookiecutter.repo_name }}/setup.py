#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django==1.8.7',
    'dj-database-url==0.3.0',
    'django-braces==1.4.0',
    # django-configurations 0.8 does not work with Django 1.8. A fork has been
    # added to requirements/forks.pip that supports Django 1.8.
    # 'django-configurations==0.8',
    'django-crispy-forms==1.4.0',
    'django-grappelli==2.6.3',
    'django-model-utils==2.3.1',
    'envdir==0.7',
    'psycopg2==2.5.4',
    'pytz==2014.10',
]

setup(
    name='{{ cookiecutter.pkg_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    long_description=read(BASE_DIR, 'README.rst'),
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.email }}',
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],
    install_requires=requires,
    license='{{ cookiecutter.license }}',
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
