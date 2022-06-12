#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime


# In[3]:


get_ipython().system(' pip install pandas_datareader')


# In[2]:


start=datetime.datetime(2010,1,1)
end=datetime.datetime(2020,1,27)
SP500=web.DataReader(['sp500'],'fred',start,end)
SP500.dropna(inplace=True)
SP500['daily_return']=(SP500['sp500']/SP500['sp500'].shift(1))-1
SP500['daily_return'].plot(title='SP500 daily return')


# In[3]:


SP500


# In[ ]:




