#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install datetime


# In[3]:


pip install matplotlib


# In[4]:


pip install pandas


# In[5]:


pip install mpl_finance


# In[7]:


import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas_datareader as web
from mpl_finance import candlestick_ohlc

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

df = web.DataReader('AAPL','yahoo',start, end)

print(df.head())

df = df[['Open','High','Low','Close']]

df.reset_index(inplace=True)
df['Date'] = df['Date'].map(mdates.date2num)

ax = plt.subplot()
candlestick_ohlc(ax, df.values, width=8, colorup='g', colordown='r')
ax.xaxis_date()
ax.grid(True)
plt.show()

ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('AAPL Share Price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')


# In[2]:


pip install pandas_datareader


# In[ ]:




