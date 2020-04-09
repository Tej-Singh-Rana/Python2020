#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#
# to display single or double quotes arround words.
def quote_my(word):
    # checks the word starting with quotes.
    if word.startswith("\""):
        print("\'",word,"\'")
    else:
        print('\"',word,'\"')

# calling function
string = input("Enter the word : ")
quote_my(string)


# In[ ]:


#
# program check the condition in b/w white and blue color.
# if else nested conditional
color = input("enter your color name (\"White\"/\"Blue\") : ")
size = input("enter your size (\"L\",\"M\",\"S\") : ")

if color.lower() == "white":
    # matching two conditions with logical operators.
    # lower() function - convert caps to lower case.
    if size.lower() == "l" or size.lower() == "m":
        print("It's available.")
        print("your order is confirmed : ",color,", size is : ",size)
    else:
        print("It's not available.")
elif color.lower() == "blue":
    if size.lower() == 'm' or size.lower() == 's':
        print("It's available.")
        print("your order is confirmed : ",color,", size is : ",size)
    else:
        print("It's not available.")
else:
    print("Out of stock.")


# In[ ]:


#
# program check input is string or digit.
# defining function
def str_analysis(string):
    # checks string is digit or not.
    if string.isdigit():
        # putting condition
        if int(string) > 99:
            print("It's a greater than 99.")
            print("a big number.")
        else:
            print("a small number.")
    # condition for alphabets.
    # checks string is alpha or not
    elif string.isalpha():
        print("Its a alpha")
    else:
        print("neither all alpha nor all digit.")

# calling function
number = input("enter digit or alpha :")
str_analysis(number)


# In[ ]:




