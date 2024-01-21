#!/usr/bin/env python
# coding: utf-8

# In[16]:


import scipy.stats as st
import pandas as pd


# In[2]:


atkins = [6,2,3,4,2,3,3,2,7,8,10,4]
GM = [4,4,5,7,8,5,3,7,10,4,5,2]
SouthBeach = [6,7,5,6,8,7,8,9,6,5,5,12]


# In[3]:


f_stats, p_value = st.f_oneway(atkins, GM, SouthBeach)


# In[4]:


f_stats


# In[5]:


p_value


# In[7]:


if p_value<0.05:
    print("Reject null hypothesis. There is a Significient differwnce between samples")
else:
    print("Fail to Reject null hypothesis. There is no Significient differwnce between samples")


# In[13]:


df = pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/Iris.csv',index_col = 0)


# In[14]:


df


# In[18]:


f_stats, p_value = st.f_oneway(df['SepalLengthCm'], df['SepalWidthCm'], df['PetalLengthCm'], df['PetalWidthCm'])


# In[19]:


f_stats, p_value


# In[20]:


if f_stats > 1:
    print("reject null hypothesis")
else:
    print("fail to reject null hypothesis")


# In[21]:


if p_value<0.05:
    print("Reject null hypothesis. There is a Significient differwnce between samples")
else:
    print("Fail to Reject null hypothesis. There is no Significient differwnce between samples")


# In[ ]:




