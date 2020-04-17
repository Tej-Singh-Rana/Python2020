#!/bin/python3


language = ['Python', 'C++', 'Go', 'C#', 'Java']
initial = 0

while initial < len(language):
    print(str(initial) + " " + language[initial])
    if language[initial] == 'C#':
        print("Found this language in position : ",initial)
        break
    initial += 1

# else statement will run when no object found in while loop.
else:
    print("Not found in list.")
