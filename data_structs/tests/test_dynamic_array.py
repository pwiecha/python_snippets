import pytest
import sys
import random
import math
from data_structs.src.dynamic_array import DynamicArray

# for debug: print(da, vars(da), sys.getsizeof(da), sys.getsizeof(da._array))
repeat_cnt = 50


def test_direct_append_grow():
    da = DynamicArray()
    assert da._itemcnt == 0 and da._capacity == 2
    da.append(5)
    assert da._itemcnt == 1 and da._capacity == 2
    da.append(6)
    assert da._itemcnt == 2 and da._capacity == 2
    da.append(7)
    assert da._itemcnt == 3 and da._capacity == 4

def test_direct_get_set():
    da = DynamicArray()

    for i in range(10):
        da.append(i)
        assert da[i] == i

    for i in range(10):
        da[i] = 10 - i
        assert da[i] == 10 - i

def test_direct_illegal_get_set():

def test_direct_append_pop():

def test_direct_illegal_pop():


@pytest.mark.repeat(repeat_cnt)
def test_random_len_capacity():
    da = DynamicArray()
    expected_len = random.randrange(50, 101)
    for i in range(expected_len):
        da.append(random.randrange(100))
    assert len(da) == expected_len
    assert da._capacity == 2**math.ceil(math.log2(expected_len))
