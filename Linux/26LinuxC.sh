#!/bin/bash
service=$1
sudo systemctl start "$service"
sudo systemctl status "$service"
