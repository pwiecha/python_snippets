'''
Linear search algorithm
For list of len n:
Best case O(1)
Worst case O(n)
Returns first element that matches the target
'''
import algos_search_common


#@algos_search_common.time_this
def linear_search(target, sequence):
    for index, element in enumerate(sequence):
        if element == target:
            return index
    return -1

def binary_search(target, sequence):
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


if __name__ == "__main__":
    test_list_1 = [i for i in range(5000) if i % 2 == 0]
    # make a decorator of this pattern
    result = linear_search(4600, test_list_1)
    if result == -1:
        print("Not found")
    else:
        print(f"Found target at index {result}")

    print(binary_search(6, [1, 2, 3, 5, 8])) # should Fail
    print(binary_search(5, [1, 2, 3, 5, 8])) # should Pass

    # Test with timeit on sorted lists
    import timeit
    setup_code = """
from __main__ import linear_search
import random
test_list_size = 10_000
test_list = [i for i in range(test_list_size)]
"""
    algo_code = """
result = linear_search(random.randint(0, test_list_size), test_list)
"""

    linear_search_results = timeit.repeat(stmt=algo_code, setup=setup_code,
                                          number=500, repeat=10)
    print(f"Mean of linear search results {sum(linear_search_results) / len(linear_search_results)}")

#TODO measure binary search

