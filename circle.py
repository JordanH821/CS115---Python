'''
Created on Apr 24, 2012

@author: bribor
'''
from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x, y, radius, name="Circle"):
        super().__init__(x, y, name)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return math.pi * self.__radius * self.__radius

    def __str__(self):
        return super().__str__() + ", radius = " + str(self.__radius) + \
            ", area = %.3f" % self.area

if __name__ == '__main__':
    circle = Circle(20, 20, 5)
    print(circle)