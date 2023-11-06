#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

filename=$1

python3 web4.py "$filename"
python3 jpg1.py "$filename"
python3 php1.py "$filename"
