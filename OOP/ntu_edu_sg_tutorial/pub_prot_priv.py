#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python convention of public/protected/private variables
@author: pwiecha
"""

class PPPClass:
    c_pub = 555
    _c_prot = 666
    __c_priv = 777
    
    def __init__(self):
        self.i_pub = 5
        self._i_prot = 10
        self.__i_priv = 15
        self.__i_special__ = 'zxc'
    
    def get_class_priv(self):
        return self.__class__.__c_priv
        
    def get_inst_priv(self):
        return self.__i_priv
    
if __name__ == "__main__":
    # All variables still accessible, be it from method or direct
    # __-prefixed variables/attributes have their name mangled
    myinst = PPPClass()
    
    print(PPPClass.c_pub)
    print(PPPClass._c_prot)
    # print(PPPClass._c_priv) # AttributeError
    # print(PPPClass.__dict__) # found _PPPClass__c_priv
    print(PPPClass._PPPClass__c_priv) # name mangled
    
    print(myinst.i_pub)
    print(myinst._i_prot)
    # print(myinst.__i_priv)
    # print(myinst.__dict__)
    print(myinst._PPPClass__i_priv)
    print(myinst.__i_special__)
    print(f"From get_class_priv: {myinst.get_class_priv()}")
    print(f"From get_inst_priv: {myinst.get_inst_priv()}")
    
    print("More sophisticated accesses")
    print(PPPClass.get_class_priv(myinst))
    print(PPPClass.get_inst_priv(myinst))