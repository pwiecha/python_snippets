# -*- coding: ascii -*-
"""Implementations of the insertion sort: recursive and non-resursive."""
from typing import Sequence, TypeVar
TNum = TypeVar('TNum', int, float)


def insertion_sort(seq: Sequence[TNum]) -> None:
    """Sort the list-like data using insertion sort algorithm.

    Upon finding unsorted element (less in value than previous),
    it swaps it with the previous until sorted

    Args:
        seq: sequence of unsorted data to sort

    Retruns:
        None. It sorts (mutates) seq in place.

    Example:
        arr = [1, 8, 3, 5]
        insertion_sort(arr)
        >>> arr
        [1, 3, 5, 8]
    """
    for i in range(1, len(seq)):
        if seq[i] < seq[i - 1]:
            for j in range(i, 0, -1):
                if seq[j] < seq[j - 1]:
                    seq[j], seq[j - 1] = seq[j - 1], seq[j]
                else:
                    break


def insertion_sort_better(seq: Sequence[TNum]) -> None:
    """Sort the list-like data using insertion sort algorithm.

    Upon finding unsorted element (less in value than previous),
    it shifts the previous elements greater than unsorted right,
    then inserts the unsorted element in the freed space.
    This version is better in terms of algorithm design imo.

    Args:
        seq: sequence of unsorted data to sort

    Retruns:
        None. It sorts (mutates) seq in place.

    Example:
        arr = [1, 8, 3, 5]
        insertion_sort_better(arr)
        >>> arr
        [1, 3, 5, 8]
    """
    for i in range(1, len(seq)):
        cur_elem = seq[i]
        j: int = i
        while j > 0 and seq[j - 1] > cur_elem:
            seq[j] = seq[j - 1]  # shift right
            j -= 1
        seq[j] = cur_elem  # insert
