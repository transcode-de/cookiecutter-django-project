#!/bin/bash
cd my-project
git init
git config user.email "alice@example.com"
git config user.name "Alice Brown"
git add -A .
git commit -m 'Initial commit'
tox
