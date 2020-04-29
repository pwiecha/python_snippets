# -*- coding: ascii -*-
"""Implementation of a dynamic array data structure, sth like python list data structure.

Implemented based on reference implementation from Goldwasser's book."""
import ctypes


class DynamicArray():
    def __init__(self, capacity=2):
        self._itemcnt = 0
        self._capacity = capacity
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._itemcnt

    def __getitem__(self, idx):
        if not 0 <= idx < self._itemcnt:
            raise IndexError(f"{self.__class__.__name__} index out of valid range")
        return self._array[idx]

    def __setitem__(self, idx, obj):
        if not 0 <= idx < self._itemcnt:
            raise IndexError(f"{self.__class__.__name__} index out of valid range")
        self._array[idx] = obj

    def append(self, obj):
        if self._itemcnt == self._capacity:
            self._grow(2 * self._capacity)
        self._array[self._itemcnt] = obj
        self._itemcnt += 1

    def pop(self):
        if self._itemcnt <= 0:
            raise IndexError(f"{self.__class__.__name__} index out of valid range")
        popped = self._array[self._itemcnt]
        self._itemcnt -= 1
        return popped

    def _grow(self, capacity):
        new_array = self._make_array(capacity)
        new_array[:len(self._array)] = self._array
        self._array = new_array
        self._capacity = capacity

    #TODO: add shrink when _itemcnt < _capacity / 4, shrink by 2

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
