#!/usr/bin/env python
# coding: utf-8

# * def
# * function name
# * parenthesis , followed by colon

# In[ ]:


def some_function_name():
    # code here after indentation
    print("Hello function!!")# at this stage by run the code we will get none.

# after a calling a function
some_function_name()


# In[ ]:


# another example of func

def yell_it():
    phrase = "Go corona GO!!".upper()
    print(phrase)

# calling a func
yell_it()


# # Function parameters

# In[ ]:


def some_func_name(code):
    # code here to execute
    print(code)
    
some_func_name(123)
some_func_name("Programming")
some_func_name("Structure")
some_func_name("Algorithm")
type(some_func_name)


# In[ ]:


def _name(code):      # inside () defining a parameter variable
    # that will be used in function code
    print(code.upper() + "!!")   # str method
    
_name("Good Morning")       # that parameter variable got a value object


# # Default Argument

# In[ ]:


def _name(code = "Python"):    # default paramter value passed
    # function code here
    print(code.lower() + " ...")
    
_name("JAVA")    # passing a parameter value
_name()    # passing no value, it uses default value


# # Creating a function with a return value

# In[ ]:


# assign parameter
def my_msg(phrase):
    double = phrase + " & " + phrase
    return double        # assign return to a value

# function call is replaced by the return value
my_req = my_msg("Calling a return value")
my_se = my_msg("Go Goa Gone!!")
print(my_se)
print(my_req)


# In[ ]:


def my_range(phrase):
    phrase = "value added"
#     print(phrase)
    return phrase
z = my_range("@@@")
print(z)
x = my_range("???")
# my_range("Hello")
print(x)
v = my_range(1)
print(v)


# In[2]:


# example
def make_schedule(period1, period2):
    schedule = ("[1st] is "+ period1.title() + ", [2nd] is "+ period2.title())
    return schedule

student_schedule = make_schedule("mathematics", "physics")
print("schedule".upper(),student_schedule)


# In[15]:


# another example
def make_schedule(period1, period2, period3):
    schedule = print("[1st] is "+ period1.title()+ ", [2nd] is "+ period2.title()+ " , [3rd] is "+ period3.title())
    return  schedule


make_schedule("chemistry", "computer", "biology")
make_schedule("a1", "a2", "a3")
make_schedule("c1", "c2", "c3")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




