class DequeEmpty(Exception):
    """Raised when trying to dequeue an empty deque."""


class DequeFull(Exception):
    """Raised when trying to enqueue a full deque."""


class ArrayDeque(object):
    """ Deque implementation usign Python list for storage.
        Implementation is an extension of the queue data type.
        Implementation based on Goldwasser book. """

    default_capacity = 10 # class attrib

    def __init__(self):
        """ Initialize an empty deque """
        self._data = [None] * ArrayDeque.default_capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """ Return w/o removing first element from the deque.

        Raises:
            DequeEmpty if the deque is empty.
        """
        if self.is_empty():
            raise DequeEmpty("Deque is empty")
        return self._data[self._front]

    def last(self):
        """ Return w/o removing last element from the deque."""
        _back = (self._front + self._size - 1) % len(self._data) # last elem ptr
        return self._data[_back]

    def push_front(self, elem):
        """ Add new element to the front of deque.

        Raises:
            DequeFull if the deque is full.
        """
        if self._size == len(self._data):
            raise DequeFull("Trying to enqueue a full deque.")
        self._front = (self._front - 1) % len(self._data)  # circular pointer
        self._data[self._front] = elem
        self._size += 1

    def pop_front(self):
        """ Remove and return first element from the deque.

        Raises:
            DequeEmpty if the deque is empty.
        """
        if self.is_empty():
            raise DequeEmpty("Deque is empty")
        pop_val = self._data[self._front]  # direct ref to underlying elem
        self._data[self._front] = None  # optional: clear reference from deque, garbage collection
        self._front = (self._front + 1) % len(self._data)  # circular pointer
        self._size -= 1
        return pop_val

    def push_back(self, elem):
        """ Add an element to the back of the deque.

        Raises:
            DequeFull if the deque is full.
        """
        if self._size == len(self._data):
            raise DequeFull("Trying to enqueue a full deque.")
        _back = (self._front + self._size) % len(self._data) # push pointer
        self._data[_back] = elem
        self._size += 1

    def pop_back(self):
        """ Remove and return first element from the deque.

        Raises:
            DequeEmpty if the deque is empty.
        """
        if self.is_empty():
            raise DequeEmpty("Deque is empty")
        _back = (self._front + self._size - 1) % len(self._data) # pop pointer
        pop_val = self._data[_back]  # direct ref to underlying elem
        self._data[_back] = None  # optional: clear reference from deque, garbage collection
        self._size -= 1
        return pop_val

