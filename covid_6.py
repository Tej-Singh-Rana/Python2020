#!/bin/python3

import os

def func():
  x = input("enter python extention : ")
  if x == "":
    print("invalid entry.")
  elif x == '.py' or x == 'py':
    print("Valid extention!!")
  elif x.isdigit():
    print("extention must be alphabet.")
  else:
    print('enter correct extention to verified.')
  return x
func()

if func() == 'py' or func() == '.py':
  print("Don't need to add extention.")
  file = input("Enter file name to create : ")
  os.system('touch {}.py'.format(file))
  print(file +".py file created.")
else:
  print("Cannot create file.")

