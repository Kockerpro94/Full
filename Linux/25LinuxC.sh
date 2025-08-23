#!/bin/bash
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6
