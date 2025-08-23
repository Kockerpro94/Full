#!/bin/bash
echo "CPU Model: $(lscpu | grep 'Model name' | awk -F: '{print $2}' | sed 's/^ //')"
echo "Number of Cores: $(nproc)"
