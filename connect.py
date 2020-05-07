#!/bin/python

print("Enter the y/n for the details : ")
t1 = input()
if t1.lower() == "y":
    pass
elif t1.lower() == "n":
    print("See you soon!")
    exit()
else:
    print("Enter only y/n.")

while True:
    print("Press 1 to enter details : \n")
    print("Press 2 to enter number : \n")
    print("Press 3 to enter code : \n")
    print("Press 4 to quit : \n")
    press = int(input())
    if press == 1:
        name = input("Enter your name : ")
        addr = input("Etner your location: ")
        print(name,"\n",addr)
    elif press == 2:
        y = int(input("Enter your contact number : "))
        print(y)

    elif press == 3:
        z = int(input("Enter your code : "))
        print(z)
    elif press == 4:
        exit()


          
