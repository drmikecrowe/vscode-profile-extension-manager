#!/usr/bin/env bash

set -euo pipefail

profile="$1"

if [ -z "$profile" ]; then
    echo "usage: $0 profile-name"
    exit 1
fi

pending="/tmp/to-install.txt"

if [ ! -f "$pending" ]; then

    cp default.txt "$pending"

    TODO=$(ls -1b singles/ | gum choose --no-limit --header "Additional Extension Groups to install")

    for f in ${TODO}; do
        cat "singles/$f" >>"$pending"
    done
fi

clear
cat "$pending"

echo " "
echo "------------------------------------------------"
echo "Install in VSCode?"

install() {
    awk '{print $1}' $pending | xargs -n 1 code --profile "$profile" --install-extension
}

gum confirm && install
rm "$pending"
