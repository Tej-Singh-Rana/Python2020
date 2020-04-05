#!/usr/bin/env python
# coding: utf-8

# # Basic math operators
# 
# - Math basic operators
#     * + addition
#     * - subtraction
#     * * multiplication
#     * / division

# In[1]:


# operators example
print("3 + 5 =",3 + 5)
print("3 + 5 - 9 =", 3 + 5 - 9)
print("48/9 =", 48/9)
print("5*5 =", 5*5)
print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))


# In[6]:


# another example
def multiple():
    make_big = input("Enter a non-decimal number you wish were bigger: ")
    
    return int(make_big)*1000000


print("Now you have",multiple())


# In[9]:


# another example

print("15 - 43 : ",15 - 43)
print("15 * 43 : ",15 * 43)
print("156 / 12 : ",156 / 12)
print("21 / 0.5 : ",21 / 0.5)
print("( 111 + 84 ) - 45 : ",( 111 + 84 ) - 45)
print("(21 + 4 ) * 4 + 4 : ",( 21 + 4 ) * 4 + 4)


# In[16]:


# Multiplying Calculator Function
def multiply():
    def user():
        p1 = int(input("Enter first : "))
        p2 = int(input("Enter second : "))
        total = p1 * p2
        return str(total)
    return user()
z = multiply()
print("Multiply :",z)


# In[47]:


# Changed in Multiplying Calculator Function
def multiply(operator):
    try:
        p1 = float(input("Enter first : "))
        p2 = float(input("Enter second : "))
        if operator == "*":
            return p1 * p2
        elif operator == "/":
            return p1 / p2
        else:
            return "Invalid Operator"
    except Exception as e:
        return("Enter correct input")
    
print(multiply(input("Enter '/' or '*' : ")))


# In[52]:


student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")

