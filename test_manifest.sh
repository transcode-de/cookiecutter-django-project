#!/usr/bin/env bash
#
# Create a Git repository, add all project files, commit and run check-manifest.

set -o errexit
set -o nounset
set -o pipefail

cd my-project

# Create Git repository, add all files and commit
git init
git config user.email "ada@example.com"
git config user.name "Ada Lovelace"
git add -A .
git commit -m 'Initial commit'

# Run tox
tox -e manifest
