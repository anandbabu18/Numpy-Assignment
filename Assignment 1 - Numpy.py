#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

import numpy as np
rand_num = np.random.normal(0,1,25)
print(rand_num)


# In[8]:


#Create a random vector of size 30 and find the mean value.

import numpy as np
x = np.random.random(10)
m = x.mean()
print(m)


# In[11]:


#Create a 10x10 array with random values and find the minimum and maximum values.

X = np.random.random((10,10))
Xmin, Xmax = X.min(),X.max()
print(Xmin,Xmax)


# In[12]:


#Find Dot product of two arrays

import numpy as np 
f = np.array([1,2])
g = np.array([4,5])
dotproduct = np.dot(f,g)
print(dotproduct)


# In[17]:


#Concatenate following arrays along axis=0

import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[5,6]])

m= np.concatenate((x,y), axis = 0)
print(m)


# In[18]:


#How to get the common items between two python NumPy arrays?

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.intersect1d(a,b))


# In[23]:


#Sort the numpy array:

import numpy as np
arr = np.array([10,5,8,4,7,2,3,1])
arr.sort()
print('Sorted array:')
print(arr)


# In[ ]:




