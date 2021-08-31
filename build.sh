#!/bin/env bash

set -euo pipefail

version=${CIRCLE_TAG:-"-1.-1.-1"}

echo "${version}" > differently/VERSION
rm -rf dist
python setup.py bdist_wheel
rm -rf build
