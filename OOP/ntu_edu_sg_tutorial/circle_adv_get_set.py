# -*- coding: utf-8 -*-

"""
Example summary.

Circle class with undecorated get/set methods and with property methods.
@author: pwiecha
"""
import math


class Circle(object):
    """Circle class with undecorated get/set methods."""

    inst_cnt = 0

    def __init__(self, _radius=1.0):
        self.set_radius(_radius)
        self.__class__.inst_cnt += 1
        self._id = self.__class__.inst_cnt

    def __str__(self):
        return (f"Object of: {self.__class__.__name__} class, id: {self._id}, "
                f"with radius:{self.get_radius()}")

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self._radius})"

    def get_radius(self):
        return self._radius

    def set_radius(self, _radius):
        if _radius < 0:
            raise ValueError("Radius should be non-negative")
        self._radius = _radius

    def get_area(self):
        return math.pi*self.get_radius()**2


if __name__ == "__main__":
    rad = -5.0
    try:
        cb1 = Circle(rad)
    except Exception:
        print("Caught an error during Circle obj creation")
        cb1 = Circle(-rad)
    print(cb1)
    print(repr(cb1))
    print(cb1.get_radius())
    print(cb1.get_area())

    cb1.set_radius(10.2)
    print(cb1)
    print(cb1.get_radius())
    print(cb1.get_area())
