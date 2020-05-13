import pytest
import numpy as np
import math
import copy
from ..src.insertion_sort import insertion_sort
from ..src.insertion_sort import insertion_sort_better

repeat_cnt = 50

@pytest.fixture
def unsorted_short_data():
    return np.random.choice(list(range(-1000, 1001)))


def test_directed_unsorted_data():
    list_to_sort = [3, 1, 5, 2, 8, 0]
    list_to_sort_b = copy.deepcopy(list_to_sort)
    list_sorted = sorted(copy.deepcopy(list_to_sort))
    
    insertion_sort(list_to_sort)

    insertion_sort_better(list_to_sort_b)

    assert list_to_sort == list_sorted
    assert list_to_sort_b == list_sorted


def directed_sorted_data():
    pass
def directed_len_2():
    pass
def test_unsorted_data():
    pass
def test_sorted_data():
    pass