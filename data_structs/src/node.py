class Node(object):
    """ Node object for building linked lists.
        Using __slots__: fix number of attributes
        for faster access and less memory (no __dict__)
    """
    __slots__ = '_element', '_next'

    def __init__(self, element, next_node):
        self._element = element
        self._next = next_node

