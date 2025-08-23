#!/bin/bash

file=$1
if [ -f "$file" ]; then
    stat -c "Owner: %U, Group: %G, Permissions: %A" "$file"
else
    echo "File not found."
fi
