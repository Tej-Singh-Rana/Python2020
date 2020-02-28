#!/usr/bin/env python
# coding: utf-8

# In[7]:


number=int(input("Enter the number : "))
if number >1000:
    print("entered the maximum value.")        #same group
    print('-'*50)                             #same group
#else:
print("if condition statement false i will run :")      #different group if condition false then this will execute.


# In[10]:


balance=int(input())
if balance < 0:
    transfer = -balance
    # transfer enough from the backup account:
    #backupAccount = backupAccount - transfer
    balance = balance + transfer


# In[25]:


x=int(input())
if x >0:
    x1 = x + 5
    print(x1)
    #print("x value is equal to one :")
    y = x1+x
    print(y)
    #print("x value is more then five :")
 
    #print("x value is high :")
    


# Different format of IF-Elif statements :-

# In[8]:


x=int(input('enter the number : '))

if x < 1 or x > 12:
    print("enter invalid value : ")
elif x==2:
    print("This is the month of Feb :")
elif x in (4,6,1,7,9):             # x==4 or x ==6 or x==1 or x==7 or x ==9 instead of this 'in format'
    print("this month is 30 days :")
else:
    print("this month is 31 days :")


# example :-

# In[12]:


​x=int(input("enter the month : "))
if x < 1 or x > 12:
    print("invalid month selection :")
else:
    if x==2:
        print("Month of Feb : ")
    elif x in (4,6,9,11):
        print("this month is 30 days")
    else:
        print("this month is 31 days")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




