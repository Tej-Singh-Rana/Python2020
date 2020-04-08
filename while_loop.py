#!/usr/bin/env python
# coding: utf-8

# # while loop
# - forever loop
# - Infinity loop
# - Using the while True: statement results in a loop that continues to run forever
# - or, until the loop is interrupted, such as with a `break` statement.
# # break
# - a conditional can implement break to exit a while True loop.

# In[ ]:


# while True loops forever unless a break statement is used
# examples

while True:
    print("write forever, unless there is a 'break'")
    break


# In[ ]:


# the number guess code then run, 
number_guess = "0"
secret_guess = "5"

while True:
    number_guess = input("guess the number 1 to 5 : ")
    if number_guess == secret_guess:
        print("Yes", number_guess,"is correct.\n")
        break
    else:
        print(number_guess,"is incorrect.")


# In[ ]:


while True:
    weather = input("Enter weather (sunny, rainy, snowy, or quit) : ")
    print()
    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunscreen.")
        break
    elif weather.lower() == 'rainy':
        print("Bring an umbrella and boots.")
        break
    elif weather.lower() == 'snowy':
        print("Wear warm woolean coat and boots.")
        break
    elif weather.lower().startswith('q'):
        print('"quit", detected, exiting')
        break
    else:
        print("Sorry, not sure what to suggest for ", weather + "\n")
        


# In[ ]:


# Get name program with help of while loop
familar_name = ""
while True:
    familar_name = input('Enter common name of friends/family : ')
    if familar_name.isalpha():
        if familar_name == "zack":
            print("Hello ",familar_name)
            break
        else:
            print("Try more")
    else:
        print("enter valid name.")


# In[ ]:


# name = input("Enter your first name : ") forever loop
while True:
    name = input("Enter your first name : ")
    if name.isalpha():
        break
    else:
        print(name, "is not a single word \n")
        
print("Hello ",name )


# In[ ]:


# Incrementing a variable

votes = 5


# In[ ]:


votes = votes + 1
print(votes)

# shorthand method votes = votes + 2
votes += 2
print(votes)


# In[ ]:


# Decrementing a variable

votes = 10


# In[ ]:


votes = votes -1
print(votes)

# shorthand method
votes -= 2
print(votes)


# In[ ]:


# examples
seat_count = 0

while True:
    print("seat count :",seat_count)
    seat_count = seat_count + 1
    
    if seat_count >= 5:
        print()
        break


# In[ ]:


# the SEAT TYPE COUNT code then run entering: hard, soft, medium and exit
# initialize variables
seat_count = 0
soft_seats = 0
hard_seats = 0
num_seats = 4

while True:
    seat_type = input('enter seat type of "hard","soft" or "exit" (to finish) : ')
    # if seat_type is in capital letter it will convert into lower case
    if seat_type.lower().startswith('e'):
        print()
        break
    elif seat_type.lower() == "hard":
        hard_seats += 1
    elif seat_type.lower() == "soft":
        soft_seats += 1
    else:
        print("invalid entry: counted as hard")
        hard_seats += 1
    seat_count += 1
    print(seat_count)
    if seat_count >= num_seats:
        print("\nSeats are full.")
        break

print(seat_count, "Seats Total : ", hard_seats, "hard and ", soft_seats, "soft")


# In[ ]:


# example
# Assigning hard coded values.
S = 0
M = 0
L = 0
other = 0
total = 0
scost = 6
mcost = 7
lcost = 8
while True:
    size = input("Enter the size of shirt (S,M,L) or exit : ")
    if size.lower().startswith('e'):
        print()
        break
    elif size.lower() == "s":
        S += 1
    elif size.lower() == "m":
        M += 1
    elif size.lower() == "l":
        L += 1
    elif size.isalnum():
        print("enter above shirt size.")
        other += 1
    total += 1
print("Total counts of each size & others category :-- \n")
print("S count ", S, "M count ", M, "L count", L, "others ", other)
print("Total price of S ", S*scost) 
print("Total price of M ", M*mcost)
print("Total price of L ", L*lcost )
    


# In[ ]:




