import pytest
import random
from data_structs.src.stack import ArrayStack, ArrayStackMaxlen
from data_structs.src.stack import ArrayStackEmpty, ArrayStackFull
from data_structs.src.linked_lists import LinkedStack
from data_structs.src.linked_lists import LinkedObjEmpty


@pytest.mark.parametrize("s", [ArrayStack(), ArrayStackMaxlen(), ArrayStackMaxlen(10), LinkedStack()])
def test_direct(s):
    #s = ArrayStack()  # Stack: []
    assert len(s) == 0
    s.push(5)  # Stack: [5]
    s.push(3)  # Stack: [5, 3]
    assert len(s) == 2
    assert s.top() == 3  # Stack: [5, 3]
    assert s.pop() == 3  # Stack: [5]
    assert s.pop() == 5  # Stack: []
    assert s.is_empty()  # True

    with pytest.raises(LinkedObjEmpty if isinstance(s, LinkedStack) else ArrayStackEmpty):
        s.pop()

    with pytest.raises(LinkedObjEmpty if isinstance(s, LinkedStack) else ArrayStackEmpty):
        s.top()


def test_direct_arr_maxlen():
    s = ArrayStackMaxlen()
    smax = ArrayStackMaxlen(10)

    assert len(s) == 0
    assert len(smax) == 0

    assert s.is_empty()
    assert smax.is_empty()

    for i in range(10):
        assert not s.is_full()
        assert not smax.is_full()
        s.push(i)
        smax.push(i)

    assert not s.is_full()
    assert smax.is_full()  # maxlen reached

    s.push(0)
    with pytest.raises(ArrayStackFull):
        smax.push(0)


@pytest.mark.parametrize("s", [ArrayStack(), ArrayStackMaxlen(), ArrayStackMaxlen(10), LinkedStack()])
def test_direct_is_empty(s):
    assert s.is_empty()
    s.push(1)
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()


@pytest.mark.parametrize("s", [ArrayStack(), ArrayStackMaxlen(), ArrayStackMaxlen(10), LinkedStack()])
def test_direct_pop(s):
    for i in range(15):
        s.push(i)
        assert s.pop() == i
    with pytest.raises(LinkedObjEmpty if isinstance(s, LinkedStack) else ArrayStackEmpty):
        s.pop()


@pytest.mark.parametrize("s", [ArrayStack(), ArrayStackMaxlen(), ArrayStackMaxlen(20), LinkedStack()])
def test_direct_push_top(s):
    cnt = 1
    for _ in range(20):
        d = random.randrange(100)
        s.push(d)
        assert s.top() == d
        assert len(s) == cnt
        cnt += 1
