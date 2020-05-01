#!/usr/bin/env python
# coding: utf-8

# 1. Define a new string

# In[2]:


str_class = "Hello Programmer!"


# In[9]:


str_class


# 2. Check what class our object has

# In[10]:


type(str_class)


# 3. View the docstring of the str class

# In[11]:


print(str_class.__doc__)


# 4. View the full list of properties and methods of str_class object

# In[ ]:


str_class.__dir__()


# 5. Explore a few of the methods above

# In[3]:


# capitalize words
str_class.capitalize()


# In[7]:


str_class.upper()


# In[8]:


str_class.lower()

