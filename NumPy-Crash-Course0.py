#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_list=[1,2,3]


# In[3]:


type(np.array(my_list))


# In[4]:


arr=np.array(my_list)


# In[5]:


arr


# In[14]:


np.arange(0,6,2)


# In[8]:


np.zeros(8)


# In[10]:


np.zeros((3,4))


# In[11]:


np.ones(4)


# In[15]:


np.linspace(0,100,5)


# In[20]:


np.random.randint(1,1000,(3,3))


# In[21]:


np.random.normal


# In[22]:


np.random.seed(101)
#Same cell to generate the same sequence
np.random.randint(0,100,10)


# In[23]:


np.random.randint(0,100,10)


# In[25]:


np.random.seed(101)
np.random.randint(0,100,10)


# In[27]:


np.random.seed(101)
arr=np.random.randint(0,100,10)
arr


# In[28]:


arr.max()


# In[29]:


arr.min()


# In[30]:


arr.mean()


# In[31]:


arr.argmax()  # the position of max


# In[32]:


arr.argmin()


# In[34]:


arr.reshape(2,5)


# In[38]:


matrix = np.arange(0,100).reshape(10,10)


# In[43]:


print(matrix)
type(matrix)


# In[44]:


matrix


# In[49]:


matrix[0,1]


# In[50]:


matrix[9,9]


# In[52]:


matrix[:,0]


# In[54]:


matrix[9,:]


# In[56]:


matrix[0:3,0:2]  #up to but not including the last slice index


# In[58]:


#masking
matrix > 50


# In[59]:


my_filter= matrix > 50  #Very interesting!!!


# In[61]:


matrix[my_filter]


# In[62]:


#Boolean Masking
matrix[matrix > 50]


# In[ ]:





# In[ ]:




