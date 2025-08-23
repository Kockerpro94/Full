#!/bin/bash
while true; do
    clear
    echo "CPU and Memory Usage:"
    top -b -n 1 | head -n 10
    sleep 1
done
