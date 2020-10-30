import pytest
import random
import math
from data_structs.src.deque import ArrayDeque
from data_structs.src.deque import DequeFull, DequeEmpty
from data_structs.src.linked_lists import LinkedDeque
from data_structs.src.linked_lists import LinkedObjEmpty

repeat_cnt = 50

@pytest.mark.parametrize("deq", [ArrayDeque(), LinkedDeque()])
def test_from_book_deque(deq):
    # Directed test from GW book
    deq.push_back(5)
    deq.push_front(3)
    deq.push_front(7)
    if isinstance(deq, ArrayDeque):
        assert 5 in deq._data and 3 in deq._data and 7 in deq._data
    else:
        assert deq._head._prev_node._element == 7 and deq._tail._next_node._element == 5
    assert len(deq) == 3
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

def test_linkeddeq_direct():
    deq = LinkedDeque()
    # extended previous test w/ some LL specific checks
    deq.push_back(5)
    deq.push_front(3)
    assert deq.first() == 3
    assert deq.last() == 5
    assert deq._head._prev_node._element == 3
    assert deq._head._prev_node._prev_node._element == 5
    assert deq._tail._next_node._element == 5
    assert deq._tail._next_node._next_node._element == 3
    assert deq.pop_front() == 3
    deq.push_front(3)
    deq.push_front(7)
    assert deq._head._prev_node._element == 7
    assert deq._head._prev_node._prev_node._element == 3
    assert deq._tail._next_node._element == 5
    assert deq._tail._next_node._next_node._element == 3
    assert len(deq) == 3
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

@pytest.mark.parametrize("deq", [ArrayDeque(), LinkedDeque()])
def test_empty_deque(deq):
    deq = ArrayDeque()
    with pytest.raises(
        DequeEmpty if isinstance(deq, ArrayDeque)
        else LinkedObjEmpty
    ):
        deq.pop_front()
    with pytest.raises(
        DequeEmpty if isinstance(deq, ArrayDeque)
        else LinkedObjEmpty
    ):
        deq.pop_back()

    deq.push_front(98)
    deq.pop_back()

    with pytest.raises(
        DequeEmpty if isinstance(deq, ArrayDeque)
        else LinkedObjEmpty
    ):
        deq.pop_front()
    with pytest.raises(
        DequeEmpty if isinstance(deq, ArrayDeque)
        else LinkedObjEmpty
    ):
        deq.pop_back()

    deq.push_back(98)
    deq.pop_front()

    with pytest.raises(
        DequeEmpty if isinstance(deq, ArrayDeque)
        else LinkedObjEmpty
    ):
        deq.pop_front()
    with pytest.raises(
        DequeEmpty if isinstance(deq, ArrayDeque)
        else LinkedObjEmpty
    ):
        deq.pop_back()

def test_full_deque():
    deq = ArrayDeque()
    for i in range(10):
        deq.push_front(i)

    with pytest.raises(DequeFull):
        deq.push_front(0)
