#!/usr/bin/env python
# coding: utf-8

# # Boolean operators in while loops
# - Using while loop
#     * with boolean comparison operators
#     * <, >
#     * <=, >=
#     * ==, !=
#     

# In[ ]:


count = 1

while count <= 5:
    print(count)
    count += 1


# In[ ]:


count = 5
while count >= 0:
    print(count)
    count -= 1


# In[ ]:


# another examples
count = 1

# loop 5 times
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1


# In[ ]:


# Using while with Boolean string tests

f_name = ""
while f_name.isalpha() == False:
    f_name = input("Enter first name (letters with no spaces) : ")

print("\n" + f_name.title(), "has been entered as first name.")


# In[ ]:


number = ""
#     number.isdigit() != True:
while number.isdigit() == False:
    number = input("Enter the positive number : ")

print(number," is a positive number.")


# In[ ]:


# Long number using while with a boolean string
import pdb    # importing debug module
int_num = input("Enter user input : ")
long_num = ""

while int_num.isdigit() == True:
    long_num += str(int_num)
  # pdb.set_trace()
    int_num = input("Enter user input : ")
    if int_num.lower().startswith('e'):
        print()
        break

print(long_num)


# In[ ]:




