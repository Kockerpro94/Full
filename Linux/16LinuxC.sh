#!/bin/bash

find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | awk '{print $9, $5}'
