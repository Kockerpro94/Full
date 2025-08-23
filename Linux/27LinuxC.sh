#!/bin/bash
service=$1
status=$(systemctl is-enabled "$service" 2>/dev/null)

if [ "$status" ]; then
    echo "Service '$service' is $status at boot."
else
    echo "Service '$service' not found."
fi
