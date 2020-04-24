# -*- coding: ascii -*-
"""Implementation of a dynamic array data structure, sth like python list data structure.
   Implemented based on reference implementation from Goldwasser's book."""
import ctypes

class DynamicArray():
    def __init__(self, capacity=2):
        self._itemcnt = 0
        self._capacity = capacity
        self._array = _make_array(self._capacity)


    def __len__(self):
        return self._itemcnt


    def __getitem__(self, idx):
        if 0 > idx <= 
        return self._array[idx]


    def __setitem__(self, idx, obj):
        if idx >= self._itemcnt:
            raise IndexError(f"{self.__name__} index out of range")
        self._array[idx] = obj
    


    def append(self, obj):
        if self._itemcnt == self._capacity:
            self._resize()
        self._array[self._itemcnt] = obj
        self._itemcnt += 1

    # TODO: add pop


    def _make_array(self, size):
        return # list w/ ctype objects - pointer like


    def _resize(self):
        self._new_arr = self._make_array(2*len(self._array))
        self._new_arr[:len(self._array)] = self._array
        self._array = self._new_arr
        # create new, bigger array 2X
        # copy current references to the new array


    