# MyModule
import math


class Circle:
    r = 1

    def __init__(self, a):
        self.r = a

    def area(self):
        area = math.pi*self.r*self.r
        return area

    def perimeter(self):
        perimeter = 2*math.pi*self.r
        return perimeter


class Triangle:
    a = 1
    b = 1
    c = 1

    def __init__(self, d, e, f):
        self.a = d
        self.b = e
        self.c = f

    def area(self):
        p = self.perimeter()/2
        area = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return area

    def perimeter(self):
        perimeter = self.a+self.b+self.c
        return perimeter


class Square:
    a = 1

    def __init__(self, b):
        self.a = b

    def area(self):
        area = self.a*self.a
        return area

    def perimeter(self):
        perimeter = 4*self.a
        return perimeter
