class QueueEmpty(Exception):
    """Raised when trying to dequeue empty queue."""

class ArrayQueue(object):
    """ FIFO queue implementation usign Python list for storage.
    Supports resize operation (enlarge and shrink).
    Implementation based on Goldwasser book. """
    default_capacity = 10 # class attrib

    def __init__(self):
        """ Initialize an empty queue """
        self._data = [None] * ArrayQueue.default_capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise QueueEmpty("Queue is empty")
        return self._data[_front]

    def dequeue(self):


class ArrayQueueResize(ArrayQueue):
    """ Enhancement to the ArrayQueue
    Supports resize operation (enlarge and shrink).
    Implementation based on Goldwasser book. """
