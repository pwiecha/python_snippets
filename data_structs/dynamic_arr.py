# -*- coding: ascii -*-
"""Implementation of a dynamic array data structure, sth like python list data structure.
   Implemented based on reference implementation from Goldwasser's book."""
import ctypes

class DynamicArray:
    def __init__(self):
        self._array = _make_array()
        self._capacity = len(_array)
        self._itemcnt = 0
    
    def __getitem__(self, idx):
        return self._array[idx]

    def __setitem__(self, idx, obj):
        # add guard for wrong index w/ itemcnt
        if idx >= self._itemcnt:
            raise IndexError(f"{self.__name__} index out of range")
        self._array[idx] = obj
    
    def __len__(self):
        return len(_array)

    def append(self, obj):
        if self._itemcnt == self._capacity:
            _resize()
        self._array
        #add obj to _array
        #if out of space -> call _resize before
        #update itemcount


    def _make_array(self):
        return # list w/ ctype objects - pointer like

    def _resize(self):
        # create new, bigger array
        # copy current references to the new array

    