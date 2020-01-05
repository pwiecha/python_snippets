#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Point class and an operator overloading example
as well as getattr/setattr functions
@author: pwiecha
"""

class Point:
    """Class representing a point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"A point with coordinates x:{self.x}, y:{self.y}"
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    
    def __add__(self, other):
        p = Point(self.x+other.x, self.y+other.y)
        return p
    
    def __mul__(self, factor):
        self.x *= factor
        self.y *= factor
        return self


if __name__ == "__main__":
    p1 = Point(0,1)
    p2 = Point(5,5)
    
    print(p1 * 3)
    print(p1+p2)
    print(p1)
    print(repr(p2))
    p3 = p1*5 + p2
    print(p3)
    
    # getattr/setattr
    print(p3.y)
    print(getattr(p3, "ydd", "not found")) # Not found
    print(hasattr(p3, "ydd")) # False
    setattr(p3, "x", 10)
    setattr(p3, "z", 17)
    print(p3.z)
    print(hasattr(p3, "z"))
    print(getattr(p3, "z"))
    delattr(p3, "z")
    print(hasattr(p3, "z"))
