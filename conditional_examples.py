#!/usr/bin/env python
# coding: utf-8

# # Conditional Examples

# In[ ]:


# Boolean string method 
# Each characters contain starting, capital one word.
favorite_book = input("Enter the title of a favorite book: ")

if favorite_book.istitle():
    print(favorite_book, "- nice capitalization in that title!")
else:
    print(favorite_book, "- consider capitalization throughout for book titles.")


# In[ ]:


# another example
a_number = input("enter a positive integer number: ")

if a_number.isdigit():
    print(a_number, "is a positive integer.")
elif a_number.isalnum():
    print(a_number, "is a combination of integer & word.")
    
# another if
if a_number.isalpha():
    print(a_number, "is more like a word.")
else:
    pass


# In[ ]:


vehicle_type = input('Enter a type of vehicle that starts with "P": ')

if vehicle_type.upper().startswith("P"):
    print(vehicle_type, 'starts with "P"')
else:
    print(vehicle_type, 'does not start with "P"')


# # Comparison Operators

# In[ ]:


# example of comparison operators with if-else conditions.
x = 21
if x > 25:
    print("x is already bigger than 25")
else:
    print("x was", x)
    x = 25
    print("now x is", x)


# In[ ]:


x = 18
if x + 18 == x + x:
    print("Pass: x + 18 is equal to", x + x)
else:
    print("Fail: x + 18 is not equal to", x + x)


# In[ ]:


x = 18
test_value = 18
if x != test_value:
    print('x is not', test_value)
else:
    print('x is', test_value)


# In[ ]:


# DON'T ASSIGN (x = 2) when you mean to COMPARE (x == 2)
x = 2

if x == 2:
    print('"==" tests for, is equal to')
else:
    pass


# In[ ]:


x = 10
y = int(input())
if y == x + x:
    print(y , " is equal to ", x + x)
    print("Condition is True")
elif y > x + x:
    print(y, ' is greater than with ', x + x)
    print("Condition is True")
else:
    print(y ," is less than", x + x)


# # String Comparisons
# - Strings can be equal == or unequal !=
# - Strings can be greater than > or less than <
# - alphabetically "A" is less than "B"
# - lower case "a" is greater than upper case "A"
# - String comparison control the flow of our program.

# In[ ]:


"hello" < "Hello"


# In[ ]:


"Aardvark" > "Zebra"


# In[ ]:


'student' != 'Student'


# In[ ]:


print("'student' >= 'Student' is", 'student' >= 'Student')


# In[ ]:


print("'student' != 'Student' is", 'student' != 'Student')


# In[ ]:


"Hello " + "World!" == "Hello World!"


# In[ ]:


"Hello" == "Hello"


# In[ ]:


msg = "Hello"

if msg == "Hello":
    print("Condition is True.")
else:
    print("Condition is False.")


# In[ ]:


greeting = "Hello"
msg = str(input("Enter string to match : "))
if greeting == msg:
    print("Condition is True.")
else:
    print("Condition is False.")


# In[ ]:


"Hello" == 'Hello'


# In[ ]:


"hello" == 'Hello'


# In[ ]:


"Hello" == Hello


# In[ ]:


# If using string comparisons
msg = "Save the world"
if msg == "save the world":
    # not match because of 's'
    print("message as expected")
else:
    print('message not as expected')


# In[ ]:


msg = "Save the world"
prediction = "save the world"
# string method to match string comparison
if msg.lower() == prediction.lower():
    print("Go corona Go!!")
else:
    print("Need more heal!!")


# In[ ]:


print("What is 8 + 13 ? ")

def user():
    que = int(input("Write your answer here :"))
    if que == 8 + 13:
        print("correct answer is ",que)
    else:
        print("incorrect answer.")
    return que

user()


# In[7]:


def tf_quiz(question, correct_ans):
    que = print("(T/F)",question)
    ans = input("Enter answer T or F : ")
    if ans == "T":
        return "correct"
    elif ans == "F":
        return "incorrect"
    return que,ans

z = tf_quiz("Should i save it?","T")
print("your answer is",z)
y = tf_quiz("Corona is a virus","T")
print("your answer is",y)


# In[ ]:




