#!/bin/bash
free -h | awk '/Mem:/ {print "Total RAM: "$2"\nAvailable RAM: "$7}'