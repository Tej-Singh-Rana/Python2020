#!/usr/bin/env python
# coding: utf-8

# # Escape sequence()
# - escape sequences all start with a backslash (\)
#     * \\   Backslash (\)
#     * \'   Single quote (')
#     * \"   Double quote (")
#     * \t   Tab
#     * \n   return or newline
# - We use escape sequences in strings - usually with print() statements

# In[2]:


# Multiple escape sequence based examples
print("Hello" + '\n' + "World!")
print ("\"\"WARNING!///")
print("\"What's that?\"")
print("one\ttwo\tthree")
print("four\tfive\tsix")


# In[3]:


# \n (new line)
print('Hello World!\nI am formatting print ')


# In[6]:


# \t (tab)
student_age = 15
student_name = "James"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t\t\t' + str(student_age))


# In[7]:


# using \" and \' (escaped quotes)
print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")


# In[8]:


# using  \\ (escaped backslash)
print("for a newline use \\n")


# In[18]:


def pre_word(word):
    if word.startswith('pre') and word.isalpha():
        return True
    else:
        return False
dec = input("enter a word that starts with \"pre\" : ")
if  pre_word(dec) is False:
    print("It's not a pre word.")
elif pre_word(dec) is not False:
    print("It's a valid pre word.")


# In[ ]:




