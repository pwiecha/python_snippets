#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inheritance, polymorphism, method overriding
@author: pwiecha
"""
import math as m

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def __str__(self):
        return f"A {self.__class__.__name__} class object"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def hello(self):
        return f"This is a message from superclass"
    
    def get_area(self):
        return m.pi*self.radius**2


class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0):
        super().__init__(radius)
        self.height = height

    def __str__(self):
        return f"A {self.__class__.__name__} class object"

    def __repr__(self):
        return f"Cylinder({self.radius}, {self.height})"
    
    def get_volume(self):
        return super().get_area() * self.height # get Circle area
    
    def get_area(self): # override get_area()
        return 2*m.pi*self.radius*self.height + 2*super().get_area()


if __name__ == "__main__":
    circ = Circle(7)
    print(repr(Circle))
    print(repr(circ))
    print(circ)
    print("Circle area:", circ.get_area())
    
    cyl = Cylinder(4, 10)
    print(cyl.hello()) # method not present -> get from superclass
    print(cyl) # __str__ overriden in cylinder
    print("Cylinder volume:", cyl.get_volume())
    print("Cylinder area:", cyl.get_area())
