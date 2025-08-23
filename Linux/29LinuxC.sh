#!/bin/bash
service=$1
sudo journalctl -u "$service" -n 50
sudo systemctl status "$service"