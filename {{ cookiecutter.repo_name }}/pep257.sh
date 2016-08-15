#!/usr/bin/env bash
#
# Find all Python files and check their docstrings with pep257.

set -o errexit
set -o nounset
set -o pipefail

find . -name '*.py' -not -path './.*/*' -not -path '*/migrations/*' -not -path './node_modules/*' -exec pep257 -s {} +
