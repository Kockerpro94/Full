#!/bin/bash
arch=$(uname -m)
if [ "$arch" = "x86_64" ]; then
    echo "System architecture: 64-bit"
else
    echo "System architecture: 32-bit"
fi