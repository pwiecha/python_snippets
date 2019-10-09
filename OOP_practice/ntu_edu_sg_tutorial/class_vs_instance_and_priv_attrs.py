#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class variables vs instance variables
+ private attributes
@author: pwiecha
"""

class AClass:
    count = 0 # class variable shared by all instances

    def __init__(self):
        self.__class__.count += 1 # or AClass.count += 1
        self.id = self.__class__.count # instance variable
        
    def get_id(self):
        return self.id
    
    def get_count(self):
        return self.__class__.count
    
if __name__ == "__main__":
    print(f"Num of AClass instances: {AClass.count}")
    print("creating instance c1")
    c1 = AClass()
    print(AClass.count)
    print(c1.__class__.count)
    print(c1.get_count())
    print(c1.get_id())
    
    print("creating instance c1")
    c2 = AClass()
    print(AClass.count)
    print(c2.__class__.count)
    print(c2.get_count())
    print(c2.get_id())
    
    print(f"Id c1: {c1.get_id()} c2: {c2.id}")