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
        deqval = self._head._element  # direct ref to underlying elem
        self._head = self._head._next_node # move pointer to previous node
        self._size -= 1
        # When emptying the queue, clear _tail reference to the last object
        if self.is_empty():
            self._tail = None
        return deqval

    def enqueue(self, element):
        """ Add an element to the back of the queue.
        """
        new = self._Node(element, None)
        # When enqueueing first element, set both pointers to it
        if self.is_empty():
            self._head = new
            self._tail = new
        else:
            self._tail._next_node = new
        self._size += 1


class CircularLinkedQueue(object):
    """ Circular FIFO Queue using singly linked list.
    Can be used for e.g. round robin schedulers.
    This implementation uses only tail pointer (end of the queue).
    Head is always one element ahead of the tail.
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
        head_node = self._tail._next_node
        return head_node._element

    def dequeue(self):
        """ Remove and return first element from the queue (FIFO).

        Raises:
            LinkedObjEmpty if the queue is empty.
        """
        if self.is_empty():
            raise LinkedObjEmpty("LinkedQueue is empty")
        old_head = self._tail._next_node
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next_node = old_head._next_node # set new head
        self._size -= 1
        return old_head._element

    def enqueue(self, element):
        """ Add an element to the back of the queue, move the tail pointer to it.
        """
        new_node = self._Node(element, None)
        # When enqueueing first element
        if self.is_empty():
            new_node._next_node = new_node # create circularity
        # Otherwise link new element and move the tail to it
        else:
            head = self._tail._next_node
            new_node._next_node = head
            self._tail._next_node = new_node
        self._tail = new_node
        self._size += 1

    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail._next_node


class _DoublyLinkedList(object):
    """ Class to be derived from - basic functionality of DLL """

    class _Node(object):
        __slots__ = "_prev_node", "_element", "_next_node"

        def __init__(self, prev_node, element, next_node):
            self._prev_node = prev_node
            self._element = element
            self._next_node = next_node

    def __init__(self):
        """ Initialize empty list with head and tail sentinels pointing to each other """
        self._tail = self._Node(None, None, None)
        self._head = self._Node(None, None, None)
        self._tail._next_node = self._head
        self._head._prev_node = self._tail
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_element(self, element, prev_n, next_n):
        """ Add element between already existing ones and return new node """
        new_n = self._Node(prev_n, element, next_n)
        prev_n._next_node = new_n
        next_n._prev_node = new_n
        self._size += 1
        return new_n

    def _delete_node(self, node):
        """ Delete node from the list and return its element """
        prev_n = node._prev_node
        next_n = node._next_node

        prev_n._next_node = next_n
        next_n._prev_node = prev_n
        self._size -= 1
        # Optional - clear reference to the deleted node
        element = node._element
        node._next_node = node._prev_node = node._element = None
        return element



