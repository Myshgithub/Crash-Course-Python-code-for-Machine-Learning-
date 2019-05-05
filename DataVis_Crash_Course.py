#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


#get_ipython().magic(u'matplotlib inline')
#just for Jupyter Notebook
#plt.show()


# In[4]:


x = np.arange(0,10)


# In[5]:


x


# In[6]:


y= x**2


# In[7]:


y


# In[38]:


plt.plot(x,y, 'r-..')


# In[50]:


plt.plot(x,y, 'cyan')
#cyan or magenta
plt.xlim(0,4)
plt.ylim(0,10)
plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")


# In[51]:


mat=np.arange(0,100).reshape(10,10)


# In[52]:


mat


# In[55]:


plt.imshow(mat, cmap='RdYlGn')


# In[56]:


mar=np.random.randint(0,1000,(10,10))


# In[61]:


mar


# In[63]:


plt.imshow(mar)
plt.colorbar()


# In[64]:


df=pd.read_csv('salaries.csv')


# In[71]:


df.plot(x='Age', y='Salary',kind='scatter')   #pandas visualization
#kind= hexbin, scatter


# In[75]:


df.plot.density(x='Salary', y='Age') #, many other plots...

