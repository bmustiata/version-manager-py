#!/usr/bin/env bash

set -e

cd $(readlink -f "$(dirname "$0")/..")

VERSION=$(version-manager --display version)

git tag -m "release $VERSION" $VERSION
git push github --tags

python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypimain

