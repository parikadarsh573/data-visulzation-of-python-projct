#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
file_path=r'C:\Users\Pc\Downloads\archive (7)\Global_Superstore2.csv'
data=pd.read_csv(file_path, encoding='latin-1')


# data

# In[6]:


data


# # data analysis

# In[7]:


data.head( ) #frist 5 rows


# In[8]:


data.shape #total number of rows &coloumn


# In[9]:


data.index # shows deatils about indering


# In[13]:


data.columns # shows coloumn names


# In[14]:


data.dtypes # shows data type of each column


# In[19]:


data.nunique() # count of the unquie value in each column


# In[20]:


data.count() #shows not null count


# # data visulaization used to show in grphically in python

# In[22]:


import matplotlib.pyplot as plt


# In[23]:


data.plot()


# In[26]:


data.plot(subplots=True)


# In[27]:


data.plot(title='global superpower')


# In[ ]:




