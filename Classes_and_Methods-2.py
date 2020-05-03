#!/usr/bin/env python
# coding: utf-8

# Arg & Kwarg

class Country():
    # args & kwargs 
    def __init__(self, name='India', pollution = 'high', environment='good' ):
        self.name = name
        self.pollution = pollution
        self.environment = environment
        
cal = Country('USA', 'average')

cal.name


cal.name


cal.environment


cal.pollution


cal.__dict__


import math

class Circle():
    is_shape = True
    
    def __init__(self, radius, color = 'red'):
        self.radius = radius
        self.color = color
        
    def area(self):
        return math.pi * self.radius ** 2
    
count = Circle(3)
count.area()


# Methods

class Pet():
    #
    def __init__(self, height):
        self.height = height
    # class attribute
    owner = "Undertaker"
    def size(self):
        return self.height >= 50
usf = Pet(height= 10)
usf.size()
usf.owner


class Number():
    is_number = 40
    def __init__(self, count):
        self.count = count
    is_odd = 50
    def compare(self, diff):
        return self.count >= diff
x = comp.is_number >= comp.is_odd
print(x)
y = comp.compare(440)
print(y)


class Pet():
    def __init__(self, height):
        self.height = height
        is_human = False
        owner = 'Michael Smith'
    def is_tall(self, tall_if_at_least):
        return self.height >= tall_if_at_least


bowser = Pet(40)
bowser.is_tall(30)


bowser.__dict__


class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq       
    def size_miles_sq(self, conversion_rate=0.621371):
        return self.size_kmsq * conversion_rate ** 2


check = Country(name='india', size_kmsq=2.382e6)
check.size_miles_sq()


print(check.size_miles_sq())


check.size_miles_sq(conversion_rate = 0.6)


# `__str__` method


class Student():
    
    def __init__(self, weight, name):
        self.name = name
        self.weight = weight


call = Student(50,'rahul')
print(call.weight,call.name)


class Student():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return '%s is good and his weight %s'%(self.name,self.weight)
    
call = Student('zack',50)
print(call)


class Student():
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def __str__(self):
        return self.name


rank = Student('Josh', 1)
print(rank)

