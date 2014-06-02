import os

from cookiecutter import prompt


if not prompt.query_yes_no('Use New BSD License for this project?'):
    os.remove('./LICENSE')
