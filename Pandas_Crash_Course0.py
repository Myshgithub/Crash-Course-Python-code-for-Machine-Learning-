#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


#print(pwd)


# In[5]:


pd.read_csv('/home/C00145769/Documents/Udemy, TensorFlow for Deep Learning with Python /salaries.csv')


# In[6]:


pd.read_csv('salaries.csv')


# In[14]:


df = pd.read_csv('salaries.csv')  #Data frame?!
print (df)


# In[19]:


df[['Salary','Name']]


# In[15]:


df[['Name','Age']]


# In[20]:


df['Salary']


# In[21]:


df['Salary'].max()


# In[22]:


df.describe()


# In[29]:


df['Salary'] > 50000  #filters


# In[30]:


df


# In[33]:


df[df['Salary'] > 50000] #Both in One line!!!


# In[34]:


df = pd.read_csv('salaries.csv')


# In[35]:


df.as_matrix()


# In[ ]:




