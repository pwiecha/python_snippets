#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class- and static- methods
@author: pwiecha
"""

class ABC:
    cls_var = "A class variable (shared among instances)"
    
    def __init__(self, some_text):
        self.inst_var = some_text
    
    def inst_method(selff): #self, cls is just a convention
        print(f"inst_method({selff} {selff.inst_var} {ABC.cls_var})")
        
    @classmethod
    def cls_method(cls):
        print(cls.cls_var)
        
    @staticmethod
    def st_method():
        print("Hello from a class!")


if __name__ == "__main__":
    print("testing inst methods")
    c1 = ABC("Instance 1 text") 
    c1.inst_method()
    ABC.inst_method(c1)

    print("testing class methods")
    ABC.cls_method()
    c1.cls_method()

    print("testing static method")
    ABC.st_method()
    c1.st_method()
    
    # CAUTION c2=ABC will alias a class not create object
    c2 = ABC("Instance 2 text") # new object
    c3 = ABC # alias

    print("\n",c2,"\n", c3)