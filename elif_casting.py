#!/usr/bin/env python
# coding: utf-8

# # Conditional elif
# - if means "if a condition exists then do some task." if is usually followed by else
# - else means "or else after we have tested if, then do an alternative task"
# - When there is a need to test for multiple conditions there is elif
# 
# - elif  statement follows  if, and means "else, if " another condition exists do something else
# - elif  can be used many times
# - else  is used after the last test condition (if or elif)
# - in pseudo code
#    * If it is raining bring an umbrella
#    * or Else If  (elif) it is snowing bring a warm coat
#    * or Else go as usual
# - else statement, the elif statement only executes when the previous if conditional is False

# # elif
#     - using string comparisons

# In[ ]:


# WHAT TO WEAR
weather = input("Enter weather (sunny, rainy, snowy, cold): ") 

if weather.lower() == "sunny":
    print("Wear a t-shirt")
elif weather.lower() == "rainy":
    print("Bring an umbrella and boots")
elif weather.lower() == "snowy":
    print("Wear a warm coat and hat")
elif weather.lower() == "cold":
    print("Wear a woolean jacket")
else:
    print("Sorry, not sure what to suggest for", weather)


# In[ ]:


# SECRET NUMBER GUESS
secret_num = "2"

guess = input("Enter a guess for the secret number (1-3): ")

if guess.isdigit() == False:
    print("Invalid: guess should only use digits")
elif guess == "1":
    print("Guess is too low")
elif guess == secret_num:
    print("Guess is right")
elif guess == "3":
    print("Guess is too high")
else:
    print(guess, "is not a valid guess (1-3)")


# In[ ]:


# examples if-elif-else condition
sale = input("Enter your size code: S, M, L ")
if sale.isalpha() == False:
    print("Invalid size code")
elif sale == "S":
    print("For S size price is $6")
elif sale == "M":
    print("For M size price is $7")
elif sale == "L":
    print("For L size price is $8")
else:
    print(sale,"is not a valid code.")


# # Casting
# - int(), str(), float()
# - `Using casting to change data type`
# - Casting is the conversion from one data type to another Such as converting from "str" to "int".
# - int() function
#     * The int() function can convert strings that represent whole counting numbers into integers and strip decimals to convert float numbers to integers.
#     * int("1") = 1 the string representing the integer character "1", cast to a number.
#     * int(5.1) = 5 the decimal (float), 5.1, truncated into a non-decimal (integer).
#     * int("5.1") = ValueError "5.1" isn't a string representation of integer, int() can cast only strings representing integer values. `ValueError: invalid literal for int() with base 10: '5.1'`

# In[ ]:


# Example

weight1 = '20'   # a string
weight2 = 170    # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)


# In[ ]:


# casting with int() & str()
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# Add the 3 numbers as integers and print the result
print(int(str_num_1) + int(str_num_2) + int_num_3)


# In[ ]:


str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# Add the 3 numbers as test strings and print the result
print(str_num_1 + str_num_2 + str(int_num_3))


# # Casting Numeric Input
# - Casting input() strings that represent numbers to integer values.

# In[ ]:


student_age = input('enter student age (integer): ')
age_next_year = int(student_age) + 1
print('Next year student will be',age_next_year)


# In[ ]:


# cast to int at input
student_age = int(input('enter student age (integer): '))
age_in_decade = student_age + 10

print('In a decade the student will be', age_in_decade)


# In[2]:


# adding calculator
p1 = input("Enter first number: ")
p2 = input("Enter second number: ")
result = int(p1) + int(p2)
print("Your two number addition is ",result)

