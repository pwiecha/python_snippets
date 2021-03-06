# -*- coding: ascii -*-
"""Implementation of a Stack abstract data structure.

Implemented based on reference implementation from Goldwasser's book.
"""


class ArrayStackEmpty(Exception):
    """Raised when trying to access empty container.

    Replaces IndexError used in stack List implementation.
    """


class ArrayStackFull(Exception):
    """Raised when pushing to .full container."""


class ArrayStack(object):
    """Stack data structure implemented using Python List class (adapter patter).

    LIFO (Last In First Out) Stack abstract data structure.

    Pop and push methods have an amortized running time of O(1).
    A typical call will run in constant time except cases when calling a method
    requires a resize of the internal list.
    In such case it will run in O(n) worst case time (n - current number of elements on the stack).
    Remaining methods have a constant running time of O(1).

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
        """Initialize an empty stack implemented as a list object."""
        self._data = []

    def push(self, e):
        """Add element e on top of the Stack."""
        self._data.append(e)

    def pop(self):
        """Remove and return last item on the Stack.

        Raises:
            ArrayStackEmpty if there is no item to return.
        """
        try:
            return self._data.pop()
        except IndexError:
            raise ArrayStackEmpty("Trying to pop an empty Stack")

    def top(self):
        """Return but not remove last item on the Stack.

        Raises:
            ArrayStackEmpty if there is no item to return.
        """
        try:
            return self._data[-1]
        except IndexError:
            raise ArrayStackEmpty("Stack is empty")

    def is_empty(self):
        """Return True is the Stack is empty."""
        return len(self._data) == 0

    def __len__(self):
        """Return number of elements on the Stack."""
        return len(self._data)


class ArrayStackMaxlen(object):
    """Stack data structure implemented using Python List class (adapter patter).

    LIFO (Last In First Out) Stack abstract data structure.
    This version includes optional maximum capacity option
    and pre-allocates the underlying list to such size.
    Such implementation will take more space O(maxlen),
    but push and pop methods will now always run in constant time O(1) (trade-off).

    Methods:
        push: adds an element to the Stack
        pop: removes top element from the Stack and returns it
        top: returns top elemente from the Stack
        is_empty: checks if the Stack is empty, returns boolean
        is_full: checks if the Stack is full, returns boolean
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

    def __init__(self, maxlen=None):
        """Initialize an empty stack implemented as a list object."""
        self._ecnt = 0  # element count
        self._maxlen = maxlen
        if self._maxlen is None:
            self._data = []
        else:
            self._data = self._maxlen * [None]

    def push(self, e):
        """Add element e on top of the Stack, increment element count.

        Raises:
            ArrayStackFull if there is no space left in the Stack for new element.
        """
        if self.is_full():
            raise ArrayStackFull("Stack is full")

        #  resize if no maxlen specified and list limit reached
        if self._maxlen is None and self._ecnt == len(self._data):
            self._data.append(e)
        else:
            self._data[self._ecnt] = e
        self._ecnt += 1

    def pop(self):
        """Return last item on the Stack, decrement element count.

        By decreasing the element count item can be overwritten by the next push.

        Raises:
            ArrayStackEmpty if there is no item to return.
        """
        if self.is_empty():
            raise ArrayStackEmpty("Stack is empty")

        self._ecnt -= 1
        return self._data[self._ecnt]

    def top(self):
        """Return but not remove last item on the Stack.

        Raises:
            ArrayStackEmpty if there is no item to return.
        """
        if self.is_empty():
            raise ArrayStackEmpty("Stack is empty")

        return self._data[self._ecnt - 1]

    def is_empty(self):
        """Return True is the Stack is empty."""
        return self._ecnt == 0

    def is_full(self):
        """Return True is the Stack is full."""
        return self._ecnt == self._maxlen if self._maxlen is not None else False

    def __len__(self):
        """Return number of elements on the Stack."""
        return self._ecnt
