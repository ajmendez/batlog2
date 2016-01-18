#!/bin/bash
HOST="$(hostname -s)"
LOGFILE="$HOME/Dropbox/data/.batlog.$HOST.dat"
TEMPFILE="$HOME/Dropbox/data/.templog.$HOST.dat"
UPTIMELOG="$HOME/Dropbox/data/.uptime.$HOST.dat"

echo "$(date '+%s') | $(date) | $(/usr/sbin/ioreg -l | egrep 'CycleCount|Capacity')" >> $LOGFILE
echo "$(date '+%s') | $(date) | $(/usr/local/bin/osx-cpu-temp)" >> $TEMPFILE
echo "$(date '+%s') | $(date) | $(uptime)" >> $UPTIMELOG
