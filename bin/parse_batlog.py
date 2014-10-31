#!/usr/bin/env python
import os
import re
import time
import json
from dateutil import parser
from datetime import datetime

FILENAME = os.path.expanduser('~/.batlog.dat')
if os.path.exists(os.path.expanduser('~/data/.batlog.dat')):
    FILENAME = os.path.expanduser('~/data/.batlog.dat')

OUTFILENAME = os.path.expanduser('~/data/batterylog/simplelog.json')
PREFIX = '    | |           '
PATTERN = '"(\w+)" = (.+)'

def parse_legacy(value):
    tmp = value.replace('=',':')
    return json.loads(tmp)

def parse_date(line):
    try:
        return time.mktime(parser.parse(line).timetuple())
    except:
        return time.mktime(datetime.fromtimestamp(int(line).timetuple()))

def parse(filename, outfile):
    out = []
    measurement = {}
    
    if os.path.exists(outfile):
        print 'Output file already exists: {}'.format(outfile)
        return
    
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith(PREFIX):
                x = line.replace(PREFIX, '').strip()
                item,value = re.match(PATTERN, x).groups()
                if item == 'LegacyBatteryInfo':
                    tmp = parse_legacy(value)
                    measurement.update(tmp)
                else:
                    measurement[item] = int(value)
            else:
                if len(measurement) > 0:
                    out.append(measurement)
                
                # key = time.mktime(parser.parse(line).timetuple())
                key = parse_date(line)
                measurement = dict(date=key)
    with open(outfile, 'w') as f:
        json.dump(out, f, indent=2)
                
                    



if __name__ == '__main__':
    from pysurvey import util
    util.setup_stop()
    
    parse(FILENAME, OUTFILENAME)
