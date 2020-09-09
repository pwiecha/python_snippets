class LinkedObjEmpty(Exception):
    """ Raised when trying to access an empty obj
    implemented using linked list.
    """
# Singly Linked Lists
class LinkedStack(object):
    """ LIFO Stack using singly linked list.
    All methods (push, pop) have a constant, worst case time O(1).
    It takes only as much space as its' elements occupies O(n),
    where n is current number of elements.
    """

    # Nested Node implementation
    class _Node(object):
        """ Node object for building linked lists.
        Using __slots__: fix number of attributes
        for faster access and less memory (no __dict__)
        """
        __slots__ = '_element', '_next_node'

        def __init__(self, element, next_node):
            self._element = element
            self._next_node = next_node

    # Stack methods
    def __init__(self):
        # Empty stack
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        # Create new Node and link it
        # new_head -> new_node(element, previous node)
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise LinkedObjEmpty("LinkedStack is empty!")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise LinkedObjEmpty("LinkedStack is empty!")
        popval = self._head._element
        self._head = self._head._next_node # move pointer to previous Node
        self._size -= 1
        return popval


class LinkedQueue(object):
    """ FIFO Queue using singly linked list.
    All methods have a constant running time O(1).
    Memory usage O(n), where n is current number of elements.
    """

    # Nested Node implementation
    class _Node(object):
        """ Node object for building linked lists.
        Using __slots__: fix number of attributes
        for faster access and less memory (no __dict__)
        """
        __slots__ = '_element', '_next_node'

        def __init__(self, element, next_node):
            self._element = element
            self._next_node = next_node

    # Queue methods
    def __init__(self):
        """ Initialize an empty queue.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """ Return w/o remove first element from the queue.

        Raises:
            LinkedObjEmpty if the queue is empty.
        """
        if self.is_empty():
            raise LinkedObjEmpty("LinkedQueue is empty")
        return self._head._element

    def dequeue(self):
        """ Remove and return first element from the queue (FIFO).

        Raises:
            LinkedObjEmpty if the queue is empty.
        """
        if self.is_empty():
            raise LinkedObjEmpty("LinkedQueue is empty")
        retval = self._head._element  # direct ref to underlying elem
        self._head = self._head._next_node # move pointer to previous node
        self._size -= 1
        return retval

    def enqueue(self, element):
        """ Add an element to the back of the queue.
        """
        new = self._Node(element, None)
        # TODO when queue is empty tail point to None, cannot access next node
        self._tail._next_node = new
        self._size += 1

