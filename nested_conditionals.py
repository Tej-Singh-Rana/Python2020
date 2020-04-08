#!/usr/bin/env python
# coding: utf-8

# # Nested Conditionals
# <pre>
#  if
#    if
#     if
#     else
#    else
#  else</pre>

# In[ ]:


# Nested if conditionals allow us to make subdecisions in our code.
sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego Cheese sandwich")
    else:
        print("Invalid selection.")

elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special")
else:
    print("Invalid selection.")


# In[ ]:


hello = input("type board y/n : ")
if hello == 'y':
    hi = input("enter y or n : ")
    if hi == 'y':
        print("Hello")
    elif hi == 'n':
        print("Hi")
elif hello == 'n':
    print("hi")
else:
    print('I know you??')


# In[ ]:


guess = input("Enter the game Y/N : ")
bird = ["parrot", "pigeon", "sparrow", "bat"]
if guess.lower() == 'y':
    print("Guess the correct bird name parrot, pigeon, sparrow, bat : ")
    bird_input = input("Enter the bird name : ")
    if bird_input in bird:
        if bird_input == "bat":
            print("guess is correct.")
        elif bird_input == "sparrow":
            print("Yes, you are near.")
            bird = input("Enter the bird name : ")
        elif bird_input == "parrot":
            print("Almost near")
            bird = input("Enter the bird name : ")
        elif bird_input == "pigeon":
            print("you tried a lot!!")
            bird = input("Enter the bird name : ")
    else:
        print("Invalid selection.")
elif guess.lower() == 'n':
        print("Not intersted today!!")
else:
    print("Wrong selection")
print("Good luck!!")    


# In[ ]:


# using while loop
guess = input("Enter the game Y/N : ")
bird = ["parrot", "pigeon", "sparrow", "bat"]
while True:
    if guess.lower() == 'y':
        print("Guess the correct bird name parrot, pigeon, sparrow, bat : ")
        bird_input = input("Enter the bird name : ")
        if bird_input in bird:
            if bird_input == "bat":
                print("guess is correct.")
                break
            elif bird_input == "sparrow":
                print("Yes, you are near.")
            elif bird_input == "parrot":
                print("almost near")
            elif bird_input == "pigeon":
                print("you are near")
        else:
            print("Invalid selection.")
    elif guess.lower() == 'n':
        print("Not intersted today!!")
        break
    else:
        print("Wrong selection")
        break
print("Good luck!!")    


# In[ ]:




