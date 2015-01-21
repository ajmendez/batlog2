#!/bin/bash

# date
LOGFILE="$HOME/data/.netlog.$(hostname -s).dat"
echo "$(date "+%s") | $(date)" >> $LOGFILE
/usr/sbin/netstat -ib >> $LOGFILE