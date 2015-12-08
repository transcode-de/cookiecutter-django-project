#!/bin/bash
cd my-project

# Create Git repository, add all files and commit
git init
git config user.email "alice@example.com"
git config user.name "Alice Brown"
git add -A .
git commit -m 'Initial commit'

# Run tox
tox -e manifest
