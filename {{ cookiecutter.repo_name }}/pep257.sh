#!/bin/bash
find . -name '*.py' -not -path './.*/*' -not -path '*/migrations/*' -not -path './node_modules/*' -exec pep257 -s {} +
