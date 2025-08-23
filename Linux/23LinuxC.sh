#!/bin/bash
process=$1
if pgrep -x "$process" > /dev/null; then
    pkill -9 "$process"
    echo "$process has been killed."
else
    echo "$process is not running."
fi
