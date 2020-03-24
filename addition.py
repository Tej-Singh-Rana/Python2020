#!/bin/python3
try:
    x = int(input())
    y = int(input())

    z = x + y
    print(z)
except ValueError:
    print("Enter the correct numeric value. ")
except SyntaxError:
    print("Enter the correct numeric value. ")

