#!/bin/python3

class User():

	is_value = 50

	def __init__(self, user, data):
		self.user = user
		self.data = data

	def __str__(self):

		return 'Hello, Welcome to this world', self.user

r1 = User('Rahul','Raw materials')
c1 = r1.__str__()
print(c1)






