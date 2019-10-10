#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Properties, getters and setters
@author: pwiecha
"""

class Temperature:
    def __init__(self, temp=0.0):
        self.set_temp(temp)

    def get_temp(self):
        print("get_temp called")
        return self.__temp

    def set_temp(self, temp):
        print("set_temp called")
        self.__temp = temp

    def del_temp(self):
        print("del_temp called")
        del self.__temp

    # one can also add get/set separately like: temp.getter(self.get_temp)
    temp = property(fget=get_temp, fset=set_temp,
                    fdel=del_temp, doc="Temperature of this object")

class TemperatureDecorated:
    def __init__(self, temp=0.0):
        self.__temp = temp

    @property
    def temp(self):
        print("Getting value")
        return self.__temp

    @temp.setter
    def temp(self, temp):
        print("Setting value")
        self.__temp = temp

    @temp.deleter
    def temp(self):
        print("Deleting value")
        del self.__temp


if __name__ == "__main__":
    t1 = Temperature(-50) # set_temp called in __init__
    print(t1.temp) # get_temp called / property
    t1.temp = 100 # set_temp called / property
    print(t1.temp) # get_temp called / property
    
    tdec = TemperatureDecorated(13)
    print(tdec.temp)
    tdec.temp = -31
    print(tdec.temp)
    del tdec.temp