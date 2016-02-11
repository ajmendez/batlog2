#!/bin/bash

# date
HOST="$(hostname -s)"
IMGFILE="$HOME/Dropbox/Photos/wakeup/wakeup_${HOST}_$(date '+%s').jpg"

#echo $IMGFILE $HOST

# does not allow for width/height
/usr/local/bin/imagesnap $IMGFILE >> /tmp/wakeup.log 2>&1
#/Users/ajmendez/Dropbox/bin/isightcapture -w 1280 -h 1024 -n 24 $IMGFILE >> /tmp/wakeup.log 2>&1

