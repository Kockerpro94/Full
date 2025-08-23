#!/bin/bash
process=$1
if pgrep -x "$process" > /dev/null; then
    ps -C "$process" -o pid,%mem,rss,cmd
else
    echo "$process is not running."
fi
