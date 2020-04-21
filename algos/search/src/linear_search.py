# -*- coding: ascii -*-
"""Implementation of the linear search."""
from typing import Sequence, TypeVar
TNum = TypeVar('TNum', int, float)


def linear_search(target: TNum, sequence: Sequence[TNum]) -> int:
    """Linear search algorithm.

    For sequence of len n:
    Best case O(1)
    Worst case O(n)

    Args:
        target: an element to look for.
        sequence: sequence of sorted data to look for element.

    Returns:
        Index of first element that matches the target
        -1 if the element is missing in the sequence
    """
    for index, element in enumerate(sequence):
        if element == target:
            return index
    return -1  # Not found
