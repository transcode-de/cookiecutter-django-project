#!/usr/bin/env bash
#
# Find all Python files and check their docstrings with pydocstyle.

set -o errexit
set -o nounset
set -o pipefail

find . -name '*.py' -not -path './.*/*' -not -path '*/migrations/*' -not -path './node_modules/*' -exec pydocstyle -s {} +
