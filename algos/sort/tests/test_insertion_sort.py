import pytest
import numpy as np
import copy
from ..src.insertion_sort import insertion_sort
from ..src.insertion_sort import insertion_sort_better

repeat_cnt = 50

@pytest.fixture
def unsorted_short_data():
    return np.random.choice(list(range(-1000, 1001)), 500)

@pytest.fixture
def unsorted_short_data_w_replace():
    return np.random.choice(list(range(-1000, 1001)), 500, replace=True)


def test_directed_unsorted_data():
    list_to_sort = [3, 1, 5, 2, 8, 0]
    list_to_sort_b = copy.deepcopy(list_to_sort)
    list_sorted = sorted(copy.deepcopy(list_to_sort))
    
    insertion_sort(list_to_sort)
    insertion_sort_better(list_to_sort_b)

    assert list_to_sort == list_sorted
    assert list_to_sort_b == list_sorted


def test_directed_sorted_data():
    list_to_sort = [3, 1, 5, 2, 8, 0]
    list_to_sort_b = copy.deepcopy(list_to_sort)
    list_sorted = sorted(copy.deepcopy(list_to_sort))
    
    insertion_sort(list_to_sort)
    insertion_sort_better(list_to_sort_b)

    assert list_to_sort == list_sorted
    assert list_to_sort_b == list_sorted

def test_directed_sorted_len_2():
    list_to_sort = [0, 1]
    list_to_sort_b = copy.deepcopy(list_to_sort)
    list_sorted = sorted(copy.deepcopy(list_to_sort))
    
    insertion_sort(list_to_sort)
    insertion_sort_better(list_to_sort_b)

    assert list_to_sort == list_sorted
    assert list_to_sort_b == list_sorted

def test_directed_unsorted_len_2():
    list_to_sort = [10, 1]
    list_to_sort_b = copy.deepcopy(list_to_sort)
    list_sorted = sorted(copy.deepcopy(list_to_sort))
    
    insertion_sort(list_to_sort)
    insertion_sort_better(list_to_sort_b)

    assert list_to_sort == list_sorted
    assert list_to_sort_b == list_sorted

@pytest.mark.repeat(repeat_cnt)
def test_unsorted_data_a(unsorted_short_data):
    _list = copy.deepcopy(unsorted_short_data)
    list_sorted = sorted(copy.deepcopy(unsorted_short_data))

    insertion_sort(_list)

    assert np.all(_list == list_sorted)

@pytest.mark.repeat(repeat_cnt)
def test_unsorted_data_b(unsorted_short_data):
    _list = copy.deepcopy(unsorted_short_data)
    list_sorted = sorted(copy.deepcopy(unsorted_short_data))

    insertion_sort_better(_list)

    assert np.all(_list == list_sorted)

@pytest.mark.repeat(repeat_cnt)
def test_unsorted_data_a_w_replace(unsorted_short_data_w_replace):
    _list = copy.deepcopy(unsorted_short_data_w_replace)
    list_sorted = sorted(copy.deepcopy(unsorted_short_data_w_replace))

    insertion_sort(_list)

    assert np.all(_list == list_sorted)

@pytest.mark.repeat(repeat_cnt)
def test_unsorted_data_b_w_replace(unsorted_short_data_w_replace):
    _list = copy.deepcopy(unsorted_short_data_w_replace)
    list_sorted = sorted(copy.deepcopy(unsorted_short_data_w_replace))

    insertion_sort_better(_list)

    assert np.all(_list == list_sorted)

def test_sorted_data():
    list_sorted = list(range(500))
    list_a = copy.deepcopy(list_sorted)
    list_b = copy.deepcopy(list_sorted)
    
    insertion_sort(list_a)
    insertion_sort_better(list_b)

    assert list_a == list_sorted
    assert list_b == list_sorted