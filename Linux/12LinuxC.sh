#!/bin/bash
file=$1
if [ -f "$file" ]; then
    size=$(stat -c%s "$file")
    echo "Size: $size bytes"
else
    echo "File not found."
fi
