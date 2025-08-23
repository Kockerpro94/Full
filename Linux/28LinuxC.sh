#!/bin/bash
service=$1
sudo systemctl restart "$service"
sudo systemctl status "$service"
