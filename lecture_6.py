#!/usr/bin/env python
# coding: utf-8

# # Lecture 6 -- pandas- Data Preprocessing

# In[1]:


import pandas as pd


# In[2]:


dff = pd.read_csv('auto.csv')


# In[5]:


dff.shape


# In[7]:


dff


# In[8]:


dff = pd.read_csv('auto.csv',header=None)  #if headings are not in file


# In[9]:


dff


# In[10]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


# In[12]:


# making columns of csv file
dff.columns=headers


# In[13]:


dff


# In[14]:


dff.head()


# In[15]:


dff.head(9)


# In[16]:


dff.describe()


# In[17]:


dff['make'].head()


# In[18]:


dff[['make','body-style','num-of-doors']].head()


# In[20]:


# print(dff.drop('make',axis=1))


# In[21]:


print(dff.min())
print(dff.max())
print(dff.mean())
print(dff.median())


# # for numerical calculations use numpy

# In[22]:


import numpy as np


# In[23]:


dff.replace('?',np.nan,inplace=True)


# In[24]:


dff


# In[25]:


dff.isnull()


# In[26]:


dff.isnull().sum()


# In[31]:


m = dff['normalized-losses'].astype('float').mean()


# In[29]:


# permanently change the type of this coloumn
# dff['normalized-losses'] = dff['normalized-losses'].astype('float')


# In[32]:


m


# In[33]:


dff['normalized-losses'].replace(np.nan,m,inplace=True)


# In[34]:


dff


# In[35]:


dff.isnull().sum()


# In[37]:


dff['num-of-doors'].head(25)


# In[38]:


dff['num-of-doors'].value_counts()


# In[41]:


dff['num-of-doors'].value_counts().max()


# In[42]:


dff['num-of-doors'].value_counts().min()


# In[44]:


mx = dff['num-of-doors'].value_counts().idxmax()


# In[45]:


mx


# In[55]:


dff['num-of-doors'].replace(np.nan,mx,inplace=True)


# In[54]:


dff.isnull().sum()


# In[50]:


mx = dff['bore'].value_counts().idxmax()


# In[51]:


mx


# In[56]:


dff['bore'].replace(np.nan,mx,inplace=True)


# In[57]:


dff.isnull().sum()


# In[58]:


mx = dff['stroke'].value_counts().idxmax()
dff['stroke'].replace(np.nan,mx,inplace=True)
dff.isnull().sum()


# In[62]:


mx = dff['horsepower'].value_counts().idxmax()
dff['horsepower'].replace(np.nan,mx,inplace=True)
dff.isnull().sum()


# In[63]:


mx = dff['peak-rpm'].value_counts().idxmax()
dff['peak-rpm'].replace(np.nan,mx,inplace=True)
dff.isnull().sum()


# In[65]:


mx = dff['price'].value_counts().idxmax()
dff['price'].replace(np.nan,mx,inplace=True)
dff.isnull().sum()


# In[ ]:




