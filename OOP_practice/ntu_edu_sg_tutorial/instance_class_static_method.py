#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class- and static- methods
@author: pwiecha
"""

class ABC:
    def inst_method(self, x):
        print(f"inst_method({self} {x})")
        
# TODO add class and instance variables, check accessibility in
        # @classmethod and @staticmethod

if __name__ == "__main__":
    c1 = ABC() 
    c1.inst_method(5)
    ABC.inst_method(c1, 5)

    
    # CAUTION c2=ABC will alias a class not create object
    c2 = ABC # alias
    c3 = ABC() # new object
    
    print("\n",c2,"\n", c3)