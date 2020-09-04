class Node(object):
    """ Node object for building linked lists.
        Using __slots__: fix number of attributes
        for faster access and less memory (no __dict__)
    """
    __slots__ = '_element', '_next'

    def __init__(self, _element, _next)
        self._element = _element
        self._next = _next
