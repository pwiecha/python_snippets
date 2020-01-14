import algos_search_common


#@algos_search_common.time_this
def linear_search(target, sequence):
    '''
    Linear search algorithm
    For list of len n:
    Best case O(1)
    Worst case O(n)
    Returns index of first element that matches the target
    Returns -1 otherwise
    '''
    for index, element in enumerate(sequence):
        if element == target:
            return index
    return -1


def binary_search(target, sequence):
    '''
    Linear search algorithm
    For list of len n:
    Best case O(1)
    Worst case O(log n)
    Returns index of first element that matches the target
    Returns -1 otherwise
    '''
    low_bound = 0
    high_bound = len(sequence)-1
    index = -1
    while (low_bound <= high_bound):
        mid_item = (high_bound + low_bound) // 2
        if sequence[mid_item] == target:
            index = mid_item
            break
        else:
            if target < sequence[mid_item]:
                high_bound = mid_item - 1
            else:
                low_bound = mid_item + 1
    return index


'''
# decorating func example
def deco(f):
    def wrap(*args, **kwargs):
        print("Inside wrap!")
        f(*args, **kwargs)
    return wrap

linear_search = deco(linear_search)
'''

if __name__ == "__main__":
    #print(linear_search.__doc__)
    #print(linear_search.__name__)
    assert linear_search(6, [1, 2, 3, 5, 8]) == -1 # should Fail
    assert linear_search(5, [1, 2, 3, 5, 8]) != -1 # should Pass
    assert binary_search(6, [1, 2, 3, 5, 8]) == -1 # should Fail
    assert binary_search(5, [1, 2, 3, 5, 8]) != -1 # should Pass
    print("No AssertionError so far means that simple testcases have passed")

    # Test with timeit on sorted lists
    import timeit
    setup_code = """
from __main__ import linear_search, binary_search
import random
test_list_size = 10_000
test_list = [i for i in range(test_list_size)]
"""
    linear_algo_code = """
linear_search(random.randint(0, test_list_size), test_list)
"""

    binary_algo_code = """
binary_search(random.randint(0, test_list_size), test_list)
"""

    # Run test suite 10 times, run code 500 times, run algorithm on test_list_size list (10k)
    linear_search_results = timeit.repeat(stmt=linear_algo_code, setup=setup_code,
                                          number=1000, repeat=10)
    print(f"Mean of linear search results {sum(linear_search_results) / len(linear_search_results)}")

    binary_search_results = timeit.repeat(stmt=binary_algo_code, setup=setup_code,
                                          number=1000, repeat=10)
    print(f"Mean of binary search results {sum(binary_search_results) / len(binary_search_results)}")
