import pytest
import random
from data_structs.src.stack import ArrayStack, ArrayStackEmpty


def test_direct():
    s = ArrayStack()  # Stack: []
    assert len(s) == 0
    s.push(5)  # Stack: [5]
    s.push(3)  # Stack: [5, 3]
    assert len(s) == 2
    assert s.top() == 3  # Stack: [5, 3]
    assert s.pop() == 3  # Stack: [5]
    assert s.pop() == 5  # Stack: []
    assert s.is_empty()

    with pytest.raises(ArrayStackEmpty):
        s.pop()


def test_direct_is_empty():
    s = ArrayStack()
    assert s.is_empty()
    s.push(1)
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()


def test_direct_pop():
    s = ArrayStack()
    for i in range(15):
        s.push(i)
        assert s.pop() == i
    with pytest.raises(ArrayStackEmpty):
        s.pop()


def test_direct_push_top():
    s = ArrayStack()
    cnt = 1
    for _ in range(20):
        d = random.randrange(100)
        s.push(d)
        assert s.top() == d
        assert len(s) == cnt
        cnt += 1
