#!/usr/bin/env python
# coding: utf-8

# In[3]:


# complex number
# Complex numbers are specified as <real part>+<imaginary part>j
z = 2 + 3j
print(z)
type(2 + 3j)


# In[4]:


1.8e308


# In[7]:


# 1.7e105
1.79e308


# # Escape sequence

# In[11]:


print("hello\vworld\tgood\aworld")


# In[19]:


print("\x456")


# In[28]:


print('\u2192 \N{rightwards arrow}')
print('\u2192 \N{leftwards arrow}')
print('\u2190 \N{downwards arrow}')
print('\u2193 \N{downwards arrow}')


# In[ ]:


# Raw strings
- A raw string literal is preceded by r or R, which specifies that escape sequences in the associated string are not translated.


# In[29]:


# Avoid escape sequence \t \a \b \n \vt \r \xhh(hex)
print(r"Hello\tWorld")


# In[35]:


print("good\\programming")
print(r"good\\programming")
print(R"good\\programming")


# In[39]:


# List --> ordered, mutable, dynamic, contain any data type, accessed by index.
# Lists can even contain complex objects, like functions, classes, and modules.
# A list can contain any number of objects, from zero to as many as your computer’s memory.

[1,2,3,4,5] == [3,4,5,1,2]


# In[51]:


[1,2,3,4,5] == [1,2,3,4,5]


# In[52]:


int


# In[47]:


def foo():
    pass


# In[49]:


import math
math


# In[50]:


len


# In[53]:


x = [int, float, foo, math]


# In[54]:


print(x)


# In[55]:


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']


# In[56]:


a[0]


# In[58]:


a[1],a[2],a[3],a[4],a[5]


# In[59]:


a[-1],a[-2],a[-3],a[3]


# In[60]:


# Slicing a[m:n] but it not includes n.
a[1:3]


# In[61]:


a[:4]


# In[62]:


a[::]


# In[63]:


a[-5:-2] == a[1:4]


# In[64]:


print(a[:4],a[0:4])


# In[65]:


len(a)


# In[66]:


print(a[2:],a[2:len(a)])


# In[67]:


print(a[:4] + a[4:])


# In[68]:


print(a[0:6:2])


# In[70]:


print(a[0:6:1])


# In[71]:


print(a[6:0:-1])


# In[76]:


print(a[:-1])
print(a[::-1])         #  reversing a list works the same way


# In[88]:


# The colon[:] syntax works for lists. However, 
# there is an important difference between how this operation works with a list and how it works with a string.

# string
s = "hello, world"
s[:]


# In[92]:


s[:] is s


# In[89]:


# list
# if a is a list, a[:] returns a new object that is a copy of a:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']


# In[90]:


a[:]


# In[91]:


a[:] is a


# In[101]:


# Several built-in functions can also be used, like "in" and "not in" operators :

print(a)
print("foo" in a)   # True
print("false" in a)  # False
print("false" not in a)   # True
print("bar" not in a)     # False


# In[107]:


# concatenation (+) and replication (*) operators :
# can concatenate only in list form.
print(a)
print(a + ["guess","login","idea"] + ["code","imagine","target"])


# In[110]:


# len(), min(), and max() functions :
print(len(a))

print(min(a))

print(max(a))

