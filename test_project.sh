#!/bin/bash
cd my-project
git init
git add -A .
git commit -m 'Initial commit'
tox
