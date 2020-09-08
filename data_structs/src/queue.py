class QueueEmpty(Exception):
    """Raised when trying to dequeue an empty queue."""


class QueueFull(Exception):
    """Raised when trying to enqueue a full queue."""


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
        """ Return w/o remove first element from the queue.

        Raises:
            QueueEmpty if the queue is empty.
        """
        if self.is_empty():
            raise QueueEmpty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """ Remove and return first element from the queue (FIFO).

        Raises:
            QueueEmpty if the queue is empty.
        """
        if self.is_empty():
            raise QueueEmpty("Queue is empty")
        popval = self._data[self._front]  # direct ref to underlying elem
        self._data[self._front] = None  # optional: clear reference from queue, garbage collection 
        self._front = (self._front + 1) % len(self._data)  # circular pointer
        self._size -= 1
        return popval

    def enqueue(self, elem):
        """ Add an element to the back of the queue.

        Raises:
            QueueFull if the queue is full.
        """
        if self._size == len(self._data):
            raise QueueFull("Trying to enqueue a full queue.")
        _back = (self._front + self._size) % len(self._data) # push pointer
        self._data[_back] = elem
        self._size += 1


class ArrayQueueResize(ArrayQueue):
    """ Enhancement to the ArrayQueue
    Supports resize operation (enlarge and shrink).
    Implementation based on Goldwasser book. """

    def enqueue(self, elem):
        """ Add an element to the back of the queue.

        Raises:
            QueueFull if the queue is full.
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)  # shrink by 2
        _back = (self._front + self._size) % len(self._data) # push pointer
        self._data[_back] = elem
        self._size += 1
    
    def _resize(self, capacity):
        """ Resize to a new list capacity """
        old_queue = self._data
        self._data = [None] * capacity
        old_queue_idx = self._front
        for idx in range(self._size): # copy existing elements
            self._data[idx] = old_queue[old_queue_idx]
            old_queue_idx = (old_queue_idx + 1) % len(old_queue)
        self._front = 0 # realign to the beggining of the resized queue to idx 0
