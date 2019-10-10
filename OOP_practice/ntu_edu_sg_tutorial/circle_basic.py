#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Circle class and a basic usage of class methods and attributes
@author: pwiecha
"""
import math


class Circle():
    """A Circle instance models a circle with a given radius"""
    # if math was imported here, one would have to reference to it as self.math
    def __init__(self, radius=1.0):
        self.radius = radius

    def __str__(self):
        return f"A circle class object with a radius of {round(self.radius, 2)}"

    def __repr__(self):
        """Repr should always represent a valid expression that can be used
           to re-create the object"""
        return (f"Circle(radius={self.radius})")

    def get_area(self):
        """Returns the area of this Circle instance"""
        return round(math.pi*self.radius*self.radius, 2)


if __name__ == "__main__":
    small_circle = Circle(15) # construct a circle
    print(small_circle.radius) # prints an attribute
    print(small_circle.get_area()) # invokes a method
    print(small_circle) # invokes __str__()
    print(repr(small_circle)) # invokes __repr__()
    print(small_circle) # invokes __str__()

    print("Instance objects vs class objects")
    print(small_circle.get_area()) # Python converts instance obj calls to
    print(Circle.get_area(small_circle)) # class object calls with inst as arg

    big_circle = Circle(72.456)
    print(repr(big_circle))
    print(big_circle)

    print(__doc__) # This module doc
    print(Circle.__doc__) # Circle class doc
    print(small_circle.__doc__) # same as above
    print(Circle.get_area.__doc__) # Circle class method doc

    print(isinstance(big_circle, Circle)) # True
    print(isinstance(small_circle, int)) # False