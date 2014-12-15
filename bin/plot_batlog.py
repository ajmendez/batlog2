#!/usr/bin/env python

import json
import pylab
import numpy as np
from datetime import datetime
from pysurvey.plot import setup, dateticks, hist, minmax, embiggen
from parse_batlog import OUTFILENAME as FILENAME
from matplotlib.dates import date2num

def make():
    tag = 'Voltage'
    tag = 'CurrentCapacity'
    data = json.load(open(FILENAME,'r'))
    date = date2num([datetime.fromtimestamp(x['date']) for x in data if len(x) > 1])
    amp  = [x[tag] for x in data if len(x) > 1]
    
    damp = np.diff(amp)
    ddate = date[:-1] + np.diff(date)/2.0
    uii = np.where(damp > 2)
    dii = np.where(damp < -2)
    print len(data)
    
    
    plot_params = dict(
        marker = 's',
        markersize=2,
        alpha=0.2,
        linestyle='_',
        markeredgewidth=0,
        markeredgecolor='none',
    )
    
    xr = embiggen(minmax(date), 0.02, 'both')
    yr = [0,7000]
    dyr = [-80,80]
    if np.max(amp) > 7000:
        yr = [0,10000]
        dyr = [-100,100]
    
    setup(figsize=(16,8))
    
    setup(subplt=(2,3,1), autoticks=True,
          xlabel='Date', xr=xr,
          ylabel=tag, yr=yr)
    pylab.plot(date, amp, **plot_params)
    dateticks('%Y-%m-%d')
    
    tmp = date % 7.0
    setup(subplt=(2,3,2), autoticks=True,
          xlabel='Day of Week', 
          xtickv=np.arange(7), xr=[-0.2,6.2], 
          xticknames='sun mon tue wed thur fri sat'.split(),
          ylabel=tag, yr=yr)
    pylab.plot(tmp, amp, **plot_params)
    
    tmp = (date % 1.0) * 24.0
    setup(subplt=(2,3,3), autoticks=True,
          xlabel='Hour of Day', xr=[-0.4,24.4],
          xtickv=np.arange(0,25,4), xtickrotate=dict(rotation=90, ha='center'),
          xticknames='mid 4am 8am noon 4pm 8pm  mid'.split(),
          ylabel=tag, yr=yr)
    pylab.plot(tmp, amp, **plot_params)
    # dateticks('%Y-%m-%d')
    
    
    
    
    setup(subplt=(2,3,4), autoticks=True, 
          xlabel='Date', xr=xr,
          ylabel='Delta', yr=dyr)
    pylab.plot(ddate, damp, **plot_params)
    dateticks('%Y-%m-%d', ha='center')
    
    
    tmp = (date % 7.0)[:-1]
    setup(subplt=(2,3,5), autoticks=True,
          xlabel='Day of Week',
          xtickv=np.arange(7), xr=[-0.2,6.2], 
          xticknames='sun mon tue wed thur fri sat'.split(),
          ylabel=tag, yr=dyr)
    pylab.plot(tmp, damp, **plot_params)
    hist(tmp[uii], np.linspace(0,7,90), alpha=0.5, norm=dyr[1], filled=True)
    hist(tmp[dii], np.linspace(0,7,90), alpha=0.5, norm=dyr[0], filled=True)
    
    tmp = ((date % 1.0) * 24.0)[:-1]
    setup(subplt=(2,3,6), autoticks=True,
          xlabel='Hour of Day', xr=[-0.4,24.4],
          xtickv=np.arange(0,25,4), xtickrotate=dict(rotation=90, ha='center'),
          xticknames='mid 4am 8am noon 4pm 8pm  mid'.split(),
          ylabel=tag, yr=dyr)
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
    