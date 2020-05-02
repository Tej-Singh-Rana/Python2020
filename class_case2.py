
import math    # importing math module
# instance method

class Circle():

    # class attribute
    is_shape = True

    def __init__(self, radius, color='red'):
        # instance attribute
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

# declaration 
circle = Circle(float(input()))
x = circle.area()
print(x)
