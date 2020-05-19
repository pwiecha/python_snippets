# -*- coding: ascii -*-
"""Implementation of a Stack abstract data structure.

Implemented based on reference implementation from Goldwasser's book.
"""


class ArrayStackEmpty(Exception):
    """Raised when trying to acess empty container.

    Replaces IndexError used in stack List implementation.
    """


class ArrayStack():
    """Stack data structure implemented using Python List class (adapter patter).

    Stack is the LIFO (Last In First Out) abstract data structure.

    Methods:
        push: adds an element to the Stack
        pop: removes top element from the Stack and returns it
        top: returns top elemente from the Stack
        is_empty: checks if the Stack is empty, return boolean
        len: returns number of elements in the Stack

    Attributes:
        _data: nonpublic List object used for Stack implementation

    Example usage:
        S = ArrayStack() # Stack: []
        S.push(5) # Stack: [5]
        S.push(3) # Stack: [5, 3]
        S.top() # returns 3, Stack: [5, 3]
        len(S) # returns 2
        S.pop() # returns 3, Stack: [5]
        S.pop() # returns 5, Stack: []
        S.is_empty() # returns True
        S.pop() # raises ArrayStackEmpty
    """

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            raise ArrayStackEmpty("Trying to pop an empty Stack")

    def top(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
