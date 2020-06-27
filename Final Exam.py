#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:37:08 2020

@author: carolyntaylor
"""


import pandas as pd

pd.options.mode.chained_assignment = None

COVID = pd.read_csv("us-states.csv")

COVID['pennsylvania_data'] = COVID['state'] == 'Pennsylvania'

COVID = COVID[COVID.pennsylvania_data == True]

del COVID['pennsylvania_data']

adj_deaths = pd.Series(COVID['deaths'])

COVID['adj_deaths'] = adj_deaths

COVID.loc[COVID['date'] == '2020-04-21', 'adj_deaths'] = COVID['adj_deaths'] - 282

COVID.loc[COVID['date'] == '2020-04-22', 'adj_deaths'] = COVID['adj_deaths'] - 297

del COVID['deaths']

import matplotlib.pyplot as plt 

import matplotlib.dates as mdates

plt.style.use('default')

COVID['Dates'] = pd.to_datetime(COVID['date'], infer_datetime_format=True)

del COVID['date']

plt.bar(COVID['Dates'], COVID['adj_deaths'], width = 0.5, color = 'b', alpha = 0.7)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Date', fontsize = 15)
plt.ylabel('Deaths', fontsize = 15)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
plt.gcf().autofmt_xdate()
plt.title('Pa. coronavirus cases and deaths')
plt.show()
