#!/usr/bin/env python
# coding: utf-8

# class_structure

# creating a new class called national
class National:
    # class attribute flag & rule
    flag = True
    rule = False

individual = National()

type(individual)

individual.rule

# Note:- Class attributes do not change between objects of the same class.

together = National()

together.rule

together.flag

class National:
    # class attribute flag & rule
    flag = False
    rule = True

leadership = National()

type(leadership)

leadership.rule

leadership.flag

# Define a new class animal and with two class attributes & docstrings:-

class Animal():
    # docstring
    '''We have to save animal, they are a part of our environment eco-system.'''
    # class attributes
    is_human = False
    environment = "good"
    '''Save animal, love animal'''


# Create an instance of this class


zebra = Animal()


# Check the is_human properties of this new instance


zebra.is_human


zebra.environment

print(zebra.__doc__)

class complex:
    def __init__(self,real, image):
        self.real = real
        self.image = image


x = complex("code","programs")


x.real


x.image


class Myclass():
    i = 20
    
    def f():
        return "Good work"


t1 = Myclass()


t1.f


t1.counter = 1
while t1.counter < 10:
    t1.counter = t1.counter * 2
print(t1.counter)


class Count:
    def __init__(self, number):
        # instance attribute
        self.number = number


press = Count(number = 10)
print(press)
print(press.number)


class Car():
    # class attribute
    color = "red"
    def __init__(self, model, year):
        # instance attribute
        self.model = model
        self.year = year


c1 = Car("xv1", 2020)
c2 = Car("xv2", 2021)
c3 = Car("vf2", 2022)
print(c1.model,c1.year)
print(c2.model,c2.year)
print(c1.color, c2.color)
print(c3.color)

