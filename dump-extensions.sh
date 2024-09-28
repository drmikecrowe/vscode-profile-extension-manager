#!/bin/bash

profile="$1"

set -euo pipefail

if [ -z "$profile" ]; then
    echo "usage: $0 profile-name"
    exit 1
fi

# Output file
output_file="vscode-extensions-with-desc.txt"
# Input file containing extension IDs, one per line
input_file="vscode-extensions.txt"

code --profile "$profile" --list-extensions | sort > "$input_file"

# Function to fetch and process extension data
get_vscode_extensions() {
    local id="$1"
    local max_page=10000
    local page_size=100
    local api_version="7.2-preview.1"

    # Flags setup (similar to the original script logic)
    local flags=33411 # Equivalent to combining all necessary flags

    for ((page = 1; page <= max_page; page++)); do
        # Construct the body for the POST request
        body=$(jq -n --arg id "$id" --argjson page "$page" --argjson page_size "$page_size" --argjson flags "$flags" \
        '{filters: [{criteria: [{filterType: 7, value: $id}], pageNumber: $page, pageSize: $page_size, sortBy: 0, sortOrder: 0}], assetTypes: [], flags: $flags}')

        # Make the POST request to fetch extension data
        response=$(curl -s -X POST "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery" \
        -H "Accept: application/json; charset=utf-8; api-version=$api_version" \
        -H "Content-Type: application/json" \
        -d "$body")

        # Check if the response is valid
        if [ -z "$response" ]; then
            echo "Error fetching data for extension $id"
            break
        fi

        # Parse extension details from the response using jq
        extensions=$(echo "$response" | jq '.results[0].extensions')

        # Check if extensions exist in the response
        if [ "$(echo "$extensions" | jq '. | length')" -eq 0 ]; then
            break
        fi

        echo "$extensions" > /tmp/extensions.json

        # Loop through each extension and extract relevant information
        echo "$extensions" | jq -r ' .[] | 
        {
            id: "\(.publisher.publisherName + "." + .extensionName)",
            lastUpdated: .lastUpdated,
            shortDescription: .shortDescription,
        } | "\(.id)\t\(.lastUpdated | split("T")[0])\t\(.shortDescription)"' >> "$output_file"

        # Break if the returned extensions are less than the page size, indicating the end of results
        if [ "$(echo "$extensions" | jq '. | length')" -lt "$page_size" ]; then
            break
        fi
    done
}

# Clear the output file
> "$output_file"

# Read the input file line by line and fetch extension details
while IFS= read -r line || [ -n "$line" ]; do
    get_vscode_extensions "$line"
done < "$input_file"

echo "Extension details have been written to $output_file"
