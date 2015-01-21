#!/bin/bash
HOST="$(hostname -s)"
LOGFILE="$HOME/data/.batlog.$HOST.dat"
TEMPFILE="$HOME/data/.templog.$HOST.dat"
UPTIMELOG="$HOME/data/.uptime.$HOST.dat"

date "+%s" >> $LOGFILE
/usr/sbin/ioreg -l | egrep "CycleCount|Capacity" >> $LOGFILE
echo "$(date '+%s') $(/usr/local/bin/osx-cpu-temp)" >> $TEMPFILE
echo "$(date '+%s') $(uptime)" >> $UPTIMELOG