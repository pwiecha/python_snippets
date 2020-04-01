import pytest
import random
from ..src import linear_search as ls
#import ..src.

@pytest.fixture
def sorted_short_data():
    return list(range(-50,51))

@pytest.fixture
def sorted_med_data():
    return list(range(-5000,5001))

@pytest.fixture
def sorted_long_data():
    return list(range(-1e5,1e5))

def rand_idx_val(sequence):
    ''' Randomly select index and element from sequence '''
    idx = random.choice(range(len(sequence)))
    return idx, sequence[idx]

@pytest.mark.linear
@pytest.mark.repeat(10)
def test_ls_short(sorted_short_data):
    idx, val = rand_idx_val(sorted_short_data)
    print(f"Searching for idx: {idx} val: {val}")
    assert idx == ls.linear_search(val, sorted_short_data)


