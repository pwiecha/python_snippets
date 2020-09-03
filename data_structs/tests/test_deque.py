import pytest
import random
import math
from data_structs.src.deque import ArrayDeque
from data_structs.src.deque import DequeFull, DequeEmpty

repeat_cnt = 50

def test_from_book_deque():
    # Directed test from GW book
    deq = ArrayDeque()

    deq.push_back(5)
    deq.push_front(3)
    deq.push_front(7)
    assert 5 in deq._data and 3 in deq._data and 7 in deq._data
    assert deq.first() == 7
    assert deq.pop_back() == 5
    assert len(deq) == 2
    assert deq.pop_back() == 3
    assert deq.pop_back() == 7
    assert deq.is_empty()
    deq.push_front(6)
    assert deq.last() == 6
    deq.push_front(8)
    assert not deq.is_empty()
    assert deq.last() == 6

def test_empty_deque():
    deq = ArrayDeque()
    with pytest.raises(DequeEmpty):
        deq.pop_front()
    with pytest.raises(DequeEmpty):
        deq.pop_back()

    deq.push_front(98)
    deq.pop_back()

    with pytest.raises(DequeEmpty):
        deq.pop_front()
    with pytest.raises(DequeEmpty):
        deq.pop_back()

    deq.push_back(98)
    deq.pop_front()

    with pytest.raises(DequeEmpty):
        deq.pop_front()
    with pytest.raises(DequeEmpty):
        deq.pop_back()

def test_full_deque():
    deq = ArrayDeque()
    for i in range(10):
        deq.push_front(i)

    with pytest.raises(DequeFull):
        deq.push_front(0)
