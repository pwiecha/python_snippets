# -*- coding: ascii -*-
"""Implementations of the insertion sort: recursive and non-resursive."""
from typing import Sequence, TypeVar
TNum = TypeVar('TNum', int, float)


def insertion_sort(seq: Sequence[TNum]) -> None:
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            for j in range(i, 0, -1):
                if seq[j] < seq[j-1]:
                    seq[j], seq[j-1] = seq[j-1], seq[j]
                else:
                    break

def insertion_sort_better(seq: Sequence[TNum]) -> None:
    for i in range(1, len(seq)):
        cur_elem = seq[i]
        j: int = i
        while j > 0 and seq[j-1] > cur_elem:
            seq[j] = seq[j-1] # shift right
            j -= 1
        seq[j] = cur_elem # insert

def insertion_sort_recursive(seq: Sequence[TNum]) -> None:
    pass

if __name__ == "__main__":
    sequence1=[3,1,5,2]
    insertion_sort_better(sequence1)
    print(sequence1, len(sequence1))
    import random
    sequence2 = random.sample(range(0, 30), 10)
    print(sequence2)
    insertion_sort_better(sequence2)
    print(sequence2)