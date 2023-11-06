#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

input_file="$1"
filename=$(basename "$input_file")
output_file="${filename%.htm}.htm"

iconv -f big5 -t utf8 "$input_file" > "$output_file"

echo "Conversion completed. Output file: $output_file"
