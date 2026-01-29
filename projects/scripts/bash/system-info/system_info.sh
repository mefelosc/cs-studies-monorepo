#!/bin/bash

# Simple System Information Script
# Author: GitHub Copilot

echo "=========================================="
echo "      SYSTEM INFORMATION REPORT"
echo "=========================================="
echo "Date/Time:   $(date)"
echo "User:        $USER"
echo "Hostname:    $(hostname)"
echo "=========================================="

echo "--- OS Information ---"
if [ -f /etc/os-release ]; then
    grep "PRETTY_NAME" /etc/os-release | cut -d'=' -f2 | tr -d '"'
else
    uname -o
fi
echo "Kernel:      $(uname -r)"
echo "Architecture: $(uname -m)"
echo ""

echo "--- System Status ---"
echo "Uptime:      $(uptime -p)"
echo "Load Average: $(cat /proc/loadavg | awk '{print $1, $2, $3}')"
echo ""

echo "--- Memory Usage ---"
free -h | awk 'NR==1{print "       " $0} NR==2{print "Mem:   " $0}'
echo ""

echo "--- Disk Usage ---"
df -h --output=source,size,used,avail,pcent,target -x tmpfs -x devtmpfs | head -n 5
echo ""

echo "--- Top 5 CPU Consuming Processes ---"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6
echo "=========================================="
