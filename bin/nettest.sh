#!/bin/bash

date

echo "$(date "+%s") | $(date)" >> ~/data/.netlog.dat
/usr/sbin/netstat -ib >> ~/data/.netlog.dat