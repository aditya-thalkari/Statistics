#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as st
import numpy as np


# In[11]:


print(st.norm.ppf(0.950,loc=0,scale=1))       #Parameter(loc) refers to mean.
print(st.norm.ppf(0.975,loc=0,scale=1))       #Parameter(Scale) refers to standard deviation.
print(st.norm.ppf(0.995,loc=0,scale=1))


# In[10]:


print(st.t.ppf(0.950,loc=0,scale=1,df=139))
print(st.t.ppf(0.975,loc=0,scale=1,df=139))
print(st.t.ppf(0.995,loc=0,scale=1,df=139))


# In[16]:


print(st.norm.interval(0.950,loc=1990,scale=2500/np.sqrt(140)))
print(st.norm.interval(scale=2500/np.sqrt(140),confidence=0.975,loc=1990))
print(st.norm.interval(confidence=0.995,loc=1990,scale=2500/np.sqrt(140)))


# In[21]:


# here
n=60
sample_mean=1000
population_standard_deviation=200

print(st.norm.interval(confidence=0.90,loc=1000,scale=200/np.sqrt(n)))      # C.I.=90percent
print(st.norm.interval(confidence=0.95,loc=1000,scale=200/np.sqrt(n)))      # C.I.=95percent
print(st.norm.interval(confidence=0.99,loc=1000,scale=200/np.sqrt(n)))      # C.I.=95percent


# In[ ]:




