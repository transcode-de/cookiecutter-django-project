import os

if '{{ cookiecutter.license|lower }}' != 'bsd':
    os.remove('./LICENSE')
