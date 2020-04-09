#!/usr/bin/env python
# coding: utf-8

# # assignment requirements
# - def
# - while
# - if,else
# - if, else(nested)
# - .isdigit()
# - .isalpha()
# - print()
# - input()

# In[1]:


# program -- string digit or alpha
# number comparison greater than, is small or big
# while loop for forever loop
def str_analysis(string):
    if string.isdigit():
        if int(string) > 99:
            print(string, "is a big number.")
        else:
            print(string,"is small number.")
    elif string.isalpha():
        print(string,"is all alphabetical characters.")
    else:
        print(string,"is neither all alpha nor all digit.")
        
value = ""
while value == "":
    value = input("Enter word or integer : ")
    
str_analysis(value)


# In[ ]:




