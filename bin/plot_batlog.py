#!/usr/bin/env python

import json
import pylab
import numpy as np
from datetime import datetime
from pysurvey.plot import setup, dateticks, hist
from parse_batlog import OUTFILENAME as FILENAME
from matplotlib.dates import date2num

def make():
    tag = 'Voltage'
    tag = 'CurrentCapacity'
    data = json.load(open(FILENAME,'r'))
    date = [datetime.fromtimestamp(x['date']) for x in data if len(x) > 1]
    amp  = [x[tag] for x in data if len(x) > 1]
    
    damp = np.diff(amp)
    ddate = date2num(date[:-1]) + np.diff(date2num(date))/2.0
    uii = np.where(damp > 2)
    dii = np.where(damp < -2)
    print len(data)
    
    
    plot_params = dict(
        marker = 's',
        markersize=2,
        alpha=0.75,
        linestyle='_',
    )
    
    yr = [0,7000]
    dyr = [-80,80]
    
    
    setup(figsize=(16,8))
    
    setup(subplt=(2,3,1), xlabel='Date', ylabel=tag, yr=yr, autoticks=True)
    pylab.plot(date, amp, **plot_params)
    dateticks('%Y-%m-%d')
    
    tmp = date2num(date) % 7.0
    setup(subplt=(2,3,2), xlabel='Day of Week', ylabel=tag, yr=yr, autoticks=True,
          xtickv=np.arange(7)+0.5, xr=[0,7], 
          xticknames='sun mon tue wed thur fri sat'.split())
    pylab.plot(tmp, amp, **plot_params)
    
    tmp = (date2num(date) % 1.0) * 24.0
    setup(subplt=(2,3,3), xlabel='Hour of Day', xr=[0,24],
          ylabel=tag, yticks=False, yr=yr, autoticks=True)
    pylab.plot(tmp, amp, **plot_params)
    # dateticks('%Y-%m-%d')
    
    
    
    
    setup(subplt=(2,3,4), xlabel='Date', ylabel='Delta', yr=dyr, autoticks=True)
    pylab.plot(ddate, damp, **plot_params)
    dateticks('%Y-%m-%d')
    
    
    tmp = (date2num(date) % 7.0)[:-1]
    setup(subplt=(2,3,5), xlabel='Day of Week', ylabel=tag, yr=dyr, autoticks=True,
          xtickv=np.arange(7)+0.5, xr=[0,7], 
          xticknames='sun mon tue wed thur fri sat'.split())
    pylab.plot(tmp, damp, **plot_params)
    hist(tmp[uii], np.linspace(0,7,90), alpha=0.5, norm=dyr[1], filled=True)
    hist(tmp[dii], np.linspace(0,7,90), alpha=0.5, norm=dyr[0], filled=True)
    
    tmp = ((date2num(date) % 1.0) * 24.0)[:-1]
    setup(subplt=(2,3,6), xlabel='Hour of Day', xr=[0,24],
          ylabel=tag, yr=dyr, autoticks=True,
          xtickv=np.arange(0,24,4), xtickrotate=90,
          xticknames='mid 4am 8am noon 4pm 8pm  '.split())
    pylab.plot(tmp, damp, **plot_params)
    hist(tmp[uii], np.linspace(0,24,50), alpha=0.5, norm=dyr[1], filled=True)
    hist(tmp[dii], np.linspace(0,24,50), alpha=0.5, norm=dyr[0], filled=True)
    # dateticks('%Y-%m-%d')
    
    
    
    # pylab.tight_layout()
    setup(hspace=0, wspace=0)
    pylab.show()
    


if __name__ == '__main__':
    from pysurvey import util
    util.setup_stop()
    
    make()
    