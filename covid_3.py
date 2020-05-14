#!/bin/python3


class Code():
	x = [1, 2, 3, 4, 5]

	def __init__(self, unicode, task=None):
		self.unicode = unicode
		self.task = task

	def main(self):
		press = int(input("Enter the unicode value [1, 2, 3, 4, 5] :- "))

		if press in x:
			print("Your code is right.")
		return press

if __name__ == "__main__":
	y = Code("unicode")
	print(y)
