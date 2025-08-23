#!/bin/bash
f1=$1
f2=$2

if [ -f "$f1" ] && [ -f "$f2" ]; then
    diff -u "$f1" "$f2"
else
    echo "One or both files not found."
fi
