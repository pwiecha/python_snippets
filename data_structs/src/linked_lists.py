class LinkedObjEmpty(Exception):
    """ Raised when trying to access an empty obj
    implemented using linked list.
    """

class LinkedStack(object):
    """ LIFO Stack using singly linked list.
    All methods (push, pop) have a constant, worst case time O(1).
    It takes only as much space as its' elements occupies.
    """

    # Nested Node implementation
    class _Node(object):
        """ Node object for building linked lists.
        Using __slots__: fix number of attributes
        for faster access and less memory (no __dict__)
        """
        __slots__ = '_element', '_next'

        def init(self, _element, _next)
            self._element = _element
            self._next = _next

    # Stack methods
    def __init__(self):
        # Empty stack
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, el):
        # Create new Node and link it.
        # Node next -> current head (previous Node)
        # Stack head -> new Node
        self._head = _Node(el, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise LinkedObjEmpty("LinkedStack is empty!")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise LinkedObjEmpty("LinkedStack is empty!")
        popval = self._head._element
        self._head = self._head._next # move pointer to previous Node
        self._size -= 1
        return popval

