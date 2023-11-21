#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Get the filename from the command line argument
filename="$1"

# Replace '?' and '=' with '.'
new_filename=$(echo "$filename" | tr '?=' '.')

# Check if the new filename already exists
if [ -e "$new_filename" ]; then
    echo "Warning: The file '$new_filename' already exists. Rename aborted."
else
    # Perform the rename using the mv command
    mv "$filename" "$new_filename"

    # Display the command that was executed
    echo "mv $filename $new_filename"
fi
