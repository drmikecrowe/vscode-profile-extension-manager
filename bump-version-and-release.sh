#!/bin/bash

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

export VERSION="$1"

rm -rf build dist

# Update version in __init__.py
sed -i "s/__version__.*/__version__ = '$VERSION'/" vpem/__init__.py

pip install -e .

# Run distribution script
python -m distribution.portable

# Commit changes
git add .
git commit -m "Bump version to $VERSION"

git push

# Create a new tag
git tag -a "v$VERSION" -m "Version $VERSION"

# Show the new tag
git show "v$VERSION"

git push origin "v$VERSION"

gh release create "v$VERSION" --generate-notes