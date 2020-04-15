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
    low_idx = 0
    high_idx = len(sequence)-1
    while low_idx <= high_idx:
        mid_idx = (high_idx + low_idx) // 2
        if target == sequence[mid_idx]:
            return mid_idx
        elif target > sequence[mid_idx]:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    return -1  # Not found


def binary_search_recursive(target: TNum, sequence: Sequence[TNum]) -> int:
    '''
    Binary search algorithm - recursive version
    For list of len n:
    Best case O(1)
    Worst case O(log n) + list slicing O(k) where k is the slice size, k < n,
    much slower than second implementation
    Args:
        target: an element to look for.
        sequence: sequence of sorted data to look for element.
    Returns:
        Index of first element that matches the target
        -1 if the element is missing in the sequence
    '''
    mid_idx = len(sequence) // 2
    # Base case - 1 element left
    if len(sequence) == 1:
        return mid_idx if target == sequence[mid_idx] else -1
    else:
        if target == sequence[mid_idx]:
            return mid_idx
        elif target > sequence[mid_idx]:
            recursive_call_result = binary_search_recursive(target, sequence[mid_idx:])
            return mid_idx + recursive_call_result if recursive_call_result != -1 else recursive_call_result
        else:
            return binary_search_recursive(target, sequence[:mid_idx])


def binary_search_recursive_two(target: TNum, sequence: Sequence[TNum]):
    def binary_search_recursive_two_inner(target: TNum, sequence: Sequence[TNum], low: int, high: int) -> int:
        '''
        Binary search algorithm - recursive version 2 w/o list slicing
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
        # Base case - searched whole sequence w/o success
        if low > high:
            return -1
        else:
            mid_idx = (low+high) // 2
            if target == sequence[mid_idx]:
                return mid_idx
            elif target > sequence[mid_idx]:
                return binary_search_recursive_two_inner(target, sequence, mid_idx+1, high)
            else:
                return binary_search_recursive_two_inner(target, sequence, low, mid_idx-1)

    return binary_search_recursive_two_inner(target, sequence, 0, len(sequence)-1)

