#!/usr/bin/env python

import json
import pylab
import numpy as np
from datetime import datetime
from pysurvey.plot import setup, dateticks
from parse_batlog import OUTFILENAME as FILENAME
from matplotlib.dates import date2num

def make():
    tag = 'Voltage'
    tag = 'CurrentCapacity'
    data = json.load(open(FILENAME,'r'))
    date = [datetime.fromtimestamp(x['date']) for x in data if len(x) > 1]
    amp  = [x[tag] for x in data if len(x) > 1]
    
    print len(data)
    
    
    setup(figsize=(18,6))
    
    setup(subplt=(1,3,1), xlabel='Date', ylabel=tag, yr=[0,7000])
    pylab.plot(date, amp, '.')
    dateticks('%Y-%m-%d')
    
    
    tmp = date2num(date) % 7.0
    setup(subplt=(1,3,2), xlabel='Day of Week', ylabel=tag, yticks=False, yr=[0,7000],
          xtickv=np.arange(7)+0.5, xr=[0,7], 
          xticknames='sun mon tue wed thur fri sat'.split())
    pylab.plot(tmp, amp, ',')
    
    
    tmp = (date2num(date) % 1.0) * 24.0
    setup(subplt=(1,3,3), xlabel='Hour of Day', xr=[0,24],
          ylabel=tag, yticks=False, yr=[0,7000])
    pylab.plot(tmp, amp, ',')
    # dateticks('%Y-%m-%d')
    
    
    pylab.show()


if __name__ == '__main__':
    from pysurvey import util
    util.setup_stop()
    
    make()
    