#!/usr/bin/env python
# coding: utf-8

# # example of function

# In[ ]:


def double_one():
    fix1 = input()
    fix2 = input()
    print(fix1, fix2, sep="\n")
    return 

double_one()


# In[ ]:


# function has a string parameter with default argument
def title_msg(msg="hello"):
    return msg
    
    
title_msg(input("Enter msg : "))


# In[ ]:


var = title_msg(input("What is the title ? "))
print("Your title is ",var)


# In[ ]:


def bookstore(book,price):
    # function code here
    return book,price

z = bookstore(input("Entry book name : "),input("Entry price of book : "))
x = bookstore(input("Entry book name : "),input("Entry price of book : "))

print(z)
print(x)


# In[ ]:


def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()
print ("Now let us see what the values of f1 and f2 are")
print (f1)
print (f2)
# RecursionError: maximum recursion depth exceeded in comparison


# In[ ]:


def say_hi(para1):
    print(para1)
#     return para1 
#     
say_hi("hello")
p = say_hi("test")
print(p)
x = say_hi("a")
z = say_hi("toy")
c = say_hi("double")
# getting None type value because function cannot pass print value instead of "return" value. 
print(c)
print(x)
print(z)


# ## Program: bird_available
# The program should ask for user to "input a bird name to check for availability" and print a statement informing of availability
# ### create this program with a Boolean function `bird_available()`
# - has parameter that takes the name of a type of bird
# - for this exercise the variable `bird_types = 'crow robin parrot eagle sandpiper hawk piegon'`
# - return `True` or `False` (we are making a Boolean function)
# - call the function using the name of a bird type from user input
# - print a sentence that indicates the availablity of the type of bird checked

# In[ ]:


# [ ] create function bird_available
def bird_available():
    bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
    return name in bird_types
# [ ] user input
name = input("Enter bird name : ")
# [ ] call bird_available
z = bird_available()
# [ ] print availbility status
print(name,"availbility status",z)


# In[ ]:


# example
# function with exception handling
def order():
    while True:
        try:
            count = int(input("How many order ? "))
            return count
        except Exception as e:
            print("Kindly enter in numbers")
            print("Example :- 1, 2, 3, 4, 5 etc..")
        finally:
            print("Thanks to choose our service.")

choice = order()
print(choice," will be ordered soon!!")


# In[10]:


# example

def order():
    try:
        count = int(input("How many order ? "))
        return count
    except Exception as e:
        print("Kindly enter in numbers")
        print("Example :- 1, 2, 3, 4, 5 etc..")
    finally:
        print("Thanks to choose our service.")

choice = order()
if choice is not None:
    print(choice, " will be ordered soon!!")


# In[ ]:




