''' Implementations of the binary search: recursive and non-resursive'''
from typing import Sequence, TypeVar
TNum = TypeVar('TNum', int, float)


def binary_search(target: TNum, sequence: Sequence[TNum]) -> int:
    '''
    Binary search algorithm
    For sorted sequence of len n:
    Best case O(1)
    Worst case O(log n)
    Args:
        target: an element to look for.
        sequence: sequence of sorted data to look for element.
    Returns:
        Index of first element that matches the target
        -1 if the element is missing in the sequence
    '''
    low_bound = 0
    high_bound = len(sequence)-1
    while low_bound <= high_bound:
        mid_item = (high_bound + low_bound) // 2
        if target < sequence[mid_item]:
            high_bound = mid_item - 1
        elif target > sequence[mid_item]:
            low_bound = mid_item + 1
        return mid_item
    return -1  # Not found


def binary_search_recursive(target: TNum, sequence: Sequence[TNum]) -> int:
    '''
    Binary search algorithm - recursive version
    For list of len n:
    Best case O(1)
    Worst case O(log n)
    Args:
        target: an element to look for.
        sequence: sequence of sorted data to look for element.
    Returns:
        Index of first element that matches the target
        -1 if the element is missing in the sequence
    '''
    low_bound = 0
    high_bound = len(sequence)-1
    if low_bound <= high_bound:
        mid_item = (high_bound + low_bound) // 2
        if target < sequence[mid_item]:
            return binary_search_recursive(target, sequence[:mid_item])
        elif target > sequence[mid_item]:
            return binary_search_recursive(target, sequence[mid_item+1:])
        return mid_item
    return -1  # Not found
