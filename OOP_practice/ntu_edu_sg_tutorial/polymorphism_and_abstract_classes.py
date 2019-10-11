#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abstract base classes example and polymorphism
@author: pwiecha
"""
from abc import abstractmethod, abstractproperty

class Animal:
    @abstractproperty
    def age(self):
        return

    @age.setter
    def age(self, new_age):
        return

    @abstractmethod
    def make_sound(self):
        pass


class Human(Animal):
    def __init__(self, age=0):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age
        
    def make_sound(self):
        return "I'm a human!"
    
class Dog(Animal):
    def __init__(self, age=0):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age
        
    def make_sound(self):
        return "Woof! Woof!"
    
if __name__ == "__main__":
    h = Human(15)
    d = Dog(3)
    for a in h, d:
        a.age = a.age * 2
        print(a.age)
        print(a.make_sound()) # two different classes, same API