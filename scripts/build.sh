#!/bin/bash

# builds a full distribution and tars it up

set -e

repo_root="$(dirname "$0")/.."

cd "$repo_root"

built_package="$("scripts/run_pyinstaller.sh")"
versioned_package="$("scripts/create_versioned_package.sh" "$built_package")"

# now tar it up
cd "$(dirname "$versioned_package")"
tar czf "$(basename "$versioned_package")".tar.gz "$(basename "$versioned_package")"
rm -rf "$(basename "$versioned_package")"
echo "$(basename "$versioned_package")".tar.gz
