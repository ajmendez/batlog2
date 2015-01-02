#!/bin/bash


date "+%s" >> ~/data/.netlog.dat
/usr/sbin/netstat -ib >> ~/data/.netlog.dat