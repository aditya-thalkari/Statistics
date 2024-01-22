#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.stats import chi2_contingency
import pandas as pd


# In[4]:


df = pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/chi2.csv',index_col=0)
df


# In[5]:


obs = pd.crosstab(index=df['Athlete'], columns=df['Smoker'])
obs


# In[7]:


chi2_stats, p_value, df, expected_freq = chi2_contingency(obs)


# In[8]:


chi2_stats, p_value


# In[10]:


if p_value < 0.05:
    print("Reject null hypothesis. cloumnas are dependent")
else:
    print("Fail to reject null hypothesis. columns are independent")


# In[ ]:




