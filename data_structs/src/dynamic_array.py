# -*- coding: ascii -*-
"""Implementation of a dynamic array data structure, sth like python list data structure.

Implemented based on reference implementation from Goldwasser's book.
"""
import ctypes


class DynamicArray():
    def __init__(self, capacity=2):
        self._itemcnt = 0
        self._capacity = capacity
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._itemcnt

    def __str__(self):
        return f"[{', '.join(str(i) for i in self._array[:self._itemcnt])}]"

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
            self._resize(2 * self._capacity)
        self._array[self._itemcnt] = obj
        self._itemcnt += 1

    def pop(self):
        try:
            popped = self._array[self._itemcnt-1]
            self._itemcnt -= 1
            if self._capacity > 4 and self._itemcnt == self._capacity // 4:
                self._resize(self._capacity // 2)
            return popped
        except (IndexError, ValueError) as err:
            print(err)
            raise # raise last exception in the current scope

    def _resize(self, capacity):
        new_array = self._make_array(capacity)
        # Shrink
        if len(self._array) > len(new_array):
            new_array = self._array[:len(new_array)]
        # Grow
        else:
            new_array[:len(self._array)] = self._array
        self._array = new_array
        self._capacity = capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
