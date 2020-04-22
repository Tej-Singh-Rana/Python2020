#!/bin/python3
import time,getpass

def user(x, y):
  if admin == "clark":
    return True
  elif password == "redhat123":
    return True
  elif admin == "" or password == "":
    print("Don't leave it blank.")
  else:
    print("Only authorized access valid.")

print("Server is up...")
time.sleep(1)
print("Connecting to the server...")
time.sleep(1)
print("Connection established.")
time.sleep(2)
admin = input("Enter name of admin : ")
password = getpass.getpass("Enter password : ") 
    
if __name__ == "__main__":
  user(admin,password)