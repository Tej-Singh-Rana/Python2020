#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(a,b):
    return a+b

var1 = add(2,5)
print(var1)


# In[ ]:


def add(a, b):
    print(a+b)
    
add(20,10)


# In[ ]:


add(50, 10)


# In[ ]:


def complex1(c, d):
    print(c*d)
    
complex1(2,5)
complex1(10,20)


# In[ ]:


def introduce(name, age, gender):
    if name == "":
        print("Name is not given.")
    else:
        print(f"Welcome {name}")
    if age <= 18 and name != "":
        print(f"{name} is {age} years old.")
    elif age >=18 and name !="":
        print("You are older.")
    sex = ["M","F","T"]

name = input("Enter your name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
var = introduce(name, age, gender)
print(var)


# In[ ]:


def introduce(name, age, gender):
    if name == "":
        print("Name is not given.")
    else:
        print(f"Welcome {name}")
    if age <= 18 and name != "":
        print(f"{name} is {age} years old.")
    elif age >=18 and name !="":
        print("You are older.")
    sex = ["M","F","T"]

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# gender = input("Enter your gender : ")
var = introduce("Carlos", 29, "T")
var1 = introduce("Tiger",25,"M")
var2 = introduce("Zack",15,"F")
# print(var)
# print(var[2])


# In[ ]:


a = "this is a string"
a = a.split(" ")
print(a)
a = "-".join(a)
print(a)


# In[ ]:


a = input()
a = a.split(" ")
print(a)
a = "-".join(a)
print(a)


# In[ ]:


a = str(input()).split(" ")
a = "-".join(a)
print(a)

