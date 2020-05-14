#!/bin/python3


class Code():
	x = [1, 2, 3, 4, 5]

	def __init__(self, unicode, task=None):
		self.unicode = unicode
		self.task = task

	def main(self):
		try:
			press = int(input("Enter the unicode value [1, 2, 3, 4, 5] :- "))
			x = [1, 2, 3, 4, 5]
			if press in x:
				return "Your code is right."
			elif press > 5:
				return "Enter digit between 1 to 5."
			else:
				return "Kindly follow procedures."
		except Exception as err:
			return "Enter only digit b/w 1 to 5."
if __name__ == "__main__":
	y = Code("one")
	z = y.main()
	print(z)
