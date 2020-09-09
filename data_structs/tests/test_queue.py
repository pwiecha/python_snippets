import pytest
import random
import math
from data_structs.src.queue import ArrayQueue, ArrayQueueResize
from data_structs.src.queue import QueueFull, QueueEmpty

repeat_cnt = 50

def test_direct_methods_queue():
    q = ArrayQueue()

    assert len(q) == 0

    q.enqueue(5)
    assert len(q) == 1
    assert q.first() == 5

    q.enqueue(3)
    assert len(q) == 2
    assert q.first() == 5

    assert q.dequeue() == 5
    assert len(q) == 1
    assert q.first() == 3

    assert q.is_empty() == False

    assert q.dequeue() == 3
    assert len(q) == 0

    with pytest.raises(QueueEmpty):
        q.first()

    assert q.is_empty() == True

    with pytest.raises(QueueEmpty):
        q.dequeue()

    assert len(q) == 0

    q.enqueue(8)
    assert len(q) == 1
    assert q.first() == 8

def test_array_full():
    q = ArrayQueue()
    qr = ArrayQueueResize()

    for idx in range(10):
        q.enqueue(random.randrange(100))
        qr.enqueue(random.randrange(100))
    with pytest.raises(QueueFull):
        q.enqueue(0)

    qr.enqueue(random.randrange(100))
    assert len(qr._data) > len(qr)
    

def test_array_resize():
    qr = ArrayQueueResize()
    initial_len = len(qr._data)
    qr.enqueue(random.randrange(100))
    qr.enqueue(random.randrange(100))
    assert len(qr._data) == initial_len // 2
    for idx in range(10):
        qr.enqueue(random.randrange(100))
    assert len(qr._data) == initial_len * 2
