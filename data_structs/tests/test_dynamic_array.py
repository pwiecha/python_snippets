import pytest
import random
import math
from data_structs.src.dynamic_array import DynamicArray

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
    print(da)


def test_direct_get_set():
    da = DynamicArray()

    for i in range(10):
        da.append(i)
        assert da[i] == i

    for i in range(10):
        da[i] = 10 - i
        assert da[i] == 10 - i


@pytest.mark.repeat(repeat_cnt)
def test_random_illegal_get_set():
    da = DynamicArray()
    repeat_val = random.randrange(10, 31)
    val_above = repeat_val + random.randrange(1, 6)
    val_below = random.randrange(-5, 0)
    illegal_idx = random.choice([val_above, val_below])

    for i in range(repeat_val):
        da.append(i)

    with pytest.raises(IndexError):
        da[illegal_idx]
        da[illegal_idx] = random.randrange(0, 11)


def test_direct_append_pop():
    da = DynamicArray()
    for _ in range(50):
        rand_val = random.randrange(100)
        itemcnt_pre_append = da._itemcnt
        da.append(rand_val)
        itemcnt_post_append = da._itemcnt
        assert itemcnt_post_append == itemcnt_pre_append + 1
        assert da.pop() == rand_val
        itemcnt_post_pop = da._itemcnt
        assert itemcnt_post_pop == itemcnt_post_append - 1


def test_direct_illegal_pop():
    da = DynamicArray()
    with pytest.raises((IndexError, ValueError)):
        da.pop()


def test_direct_grow_shrink_array():
    da = DynamicArray()
    grow_idxs = [2**i + 1 for i in range(1, 7)]
    for idx in range(1, (2**7) + 1):
        prev_capacity = da._capacity
        da.append(idx)
        new_capacity = da._capacity
        if idx in grow_idxs:
            assert new_capacity == 2 * prev_capacity

    shrink_idxs = [33, 17, 9]
    for idx in range((2**7), -1, -1):
        prev_capacity = da._capacity
        da.pop()
        new_capacity = da._capacity
        if idx in shrink_idxs:
            assert new_capacity == prev_capacity // 2


@pytest.mark.repeat(repeat_cnt)
def test_random_len_capacity():
    da = DynamicArray()
    expected_len = random.randrange(50, 101)
    for _ in range(expected_len):
        da.append(random.randrange(100))
    assert len(da) == expected_len
    assert da._capacity == 2**math.ceil(math.log2(expected_len))
