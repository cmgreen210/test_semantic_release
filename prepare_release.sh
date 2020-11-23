#!/usr/bin/env bash

set -e
set -u

echo "$1" > VERSION

python setup.py bdist_wheel sdist
