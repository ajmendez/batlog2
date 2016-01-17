#!/bin/bash

# date
HOST="$(hostname -s)"
LOGFILE="$HOME/Dropbox/data/.netlog.$HOST.dat"
LOCFILE="$HOME/Dropbox/data/.loclog.$HOST.dat"
echo "$(date '+%s') | $(date) | $(/usr/sbin/netstat -ib)" >> $LOGFILE
echo "$(date '+%s') | $(date) | $(/usr/local/bin/get-location)" >> $LOCFILE
