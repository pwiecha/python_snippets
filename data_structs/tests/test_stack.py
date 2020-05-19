import pytest
import random
import math
from data_structs.src.stack import ArrayStack, ArrayStackEmpty

def test_direct():
    s = ArrayStack() #  Stack: []
    assert len(s) == 0
    s.push(5) #  Stack: [5]
    s.push(3) #  Stack: [5, 3]
    assert len(s) == 2
    assert s.top() == 3 #  Stack: [5, 3]
    assert s.pop() == 3 #  Stack: [5]
    assert s.pop() == 5 #  Stack: []
    assert s.is_empty() == True

    with pytest.raises(ArrayStackEmpty):
        s.pop()