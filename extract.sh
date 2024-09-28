#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "Usage: $0 <category>"
    exit 1
fi

safe_filename() {
    local input="$1"

    # Replace spaces with underscores
    input="${input// /_}"

    # Remove any character that is not a letter, number, underscore, or hyphen
    input="${input//[^a-zA-Z0-9_-]/_}"

    # Optionally, you can limit the length of the filename
    # Uncomment the following line to limit to 255 characters
    # input="${input:0:255}"

    # Return the safe filename
    echo "$input"
}

input=vscode-extensions-with-desc.txt
category="$1"
outfile=$(safe_filename "$category").txt
if [ ! -z "$2" ]; then
    outfile="$2"
fi

mkdir -p backup
mkdir -p singles

cp $input backup/$input.$(date +%Y-%m-%d-%H%M%S)

rg -i "$category" $input >> singles/$outfile
rg -iv "$category" $input > /tmp/$input 
mv /tmp/$input $input

clear 
cat $input