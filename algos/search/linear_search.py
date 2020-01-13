'''
Linear search algorithm
For list of len n:
Best case O(1)
Worst case O(n)
Returns first element that matches the target
'''
from random import random
import functools

def linear_search(target, sequence):
    for index, element in enumerate(sequence):
        if element == target:
            return index
    return -1

def check_algo

if __name__ == "__main__":
    test_list1 = [i for i in range(50) if i % 2]

    # make a decorator of this pattern
    result = linear_search()
    if result is not -1:
        print(f"Found target {}")
