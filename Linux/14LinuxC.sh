#!/bin/bash
file=$1
if [ -f "$file" ]; then
    chmod +x "$file"
    echo "$file is now executable."
else
    echo "File not found."
fi