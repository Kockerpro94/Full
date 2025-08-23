#!/bin/bash
process=$1
pid=$(pgrep -x "$process")

if [ -n "$pid" ]; then
    echo "$process is running with PID(s): $pid"
else
    echo "$process is not running."
fi
