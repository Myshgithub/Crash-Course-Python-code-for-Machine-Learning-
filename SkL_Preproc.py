#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SciKit Learn Preprocessing
import numpy as np


# In[3]:


from sklearn.preprocessing import MinMaxScaler


# In[10]:


data=np.random.randint(0,100,(10,2))


# In[11]:


data


# In[12]:


#scaling Data for Neural Network...
scaler_model = MinMaxScaler()


# In[13]:


type(scaler_model)


# In[14]:


scaler_model.fit(data)


# In[15]:


scaler_model.transform(data)


# In[17]:


scaler_model.fit_transform(data)  #in one line


# In[18]:


#Splitting Data into 2 sets: Training and Data sets
import pandas as pd


# In[19]:


dataf = pd.DataFrame (data=np.random.randint(0,101,(50,4)))  


# In[20]:


dataf


# In[28]:


dataf0 = pd.DataFrame (data=np.random.randint(0,101,(50,4)), columns=['f1','f2','f3','label'])


# In[30]:


dataf0
#features, labels


# In[31]:


X=dataf0[['f1','f2','f3']]


# In[35]:


y=dataf0['label']


# In[37]:


from sklearn.model_selection import train_test_split


# In[38]:


#train_test_split


# In[40]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# In[42]:


X_train.shape


# In[43]:


X_test.shape


# In[ ]:




