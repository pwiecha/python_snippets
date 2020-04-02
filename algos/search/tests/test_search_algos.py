import pytest
import random
from ..src.linear_search import linear_search
from ..src.binary_search import binary_search
from ..src.binary_search import binary_search_recursive

@pytest.fixture
def sorted_short_data():
    return list(range(-50,51))

@pytest.fixture
def sorted_med_data():
    return list(range(-5000,5001))

@pytest.fixture
def sorted_long_data():
    return list(range(int(-1e5),int(1e5)))

def rand_idx_val(sequence):
    ''' Randomly select index and element from sequence '''
    idx = random.choice(range(len(sequence)))
    return idx, sequence[idx], f"Searching for idx: {idx} val: {sequence[idx]}"

repeat_not_found = 50
repeat_len_one = 50
repeat_short = 30
repeat_med = 20
repeat_long = 10

''' linear search testing '''

@pytest.mark.linear
@pytest.mark.repeat(repeat_short)
def test_ls_short(sorted_short_data):
    idx, val, log = rand_idx_val(sorted_short_data)
    print(log)
    assert linear_search(val, sorted_short_data) == idx

@pytest.mark.linear
@pytest.mark.repeat(repeat_med)
def test_ls_med(sorted_med_data):
    idx, val, log = rand_idx_val(sorted_med_data)
    print(log)
    assert linear_search(val, sorted_med_data) == idx

@pytest.mark.linear
@pytest.mark.repeat(repeat_long)
def test_ls_long(sorted_long_data):
    idx, val, log = rand_idx_val(sorted_long_data)
    print(log)
    assert linear_search(val, sorted_long_data) == idx

@pytest.mark.linear
@pytest.mark.repeat(repeat_not_found)
def test_ls_not_found(sorted_med_data):
    val = sorted_med_data[-1] + random.randrange(1, 50)
    assert linear_search(val, sorted_med_data) == -1

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_one)
def test_ls_len_one():
    arr = [random.randrange(1, 50)]
    assert linear_search(0, arr) == -1
    assert linear_search(arr[0], arr) == 0

# TODO: Timeit

''' binary search testing '''
''' normal '''

@pytest.mark.binary
@pytest.mark.repeat(repeat_short)
def test_bs_short(sorted_short_data):
    idx, val, log = rand_idx_val(sorted_short_data)
    print(log)
    assert binary_search(val, sorted_short_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_med)
def test_bs_med(sorted_med_data):
    idx, val, log = rand_idx_val(sorted_med_data)
    print(log)
    assert binary_search(val, sorted_med_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_long)
def test_bs_long(sorted_long_data):
    idx, val, log = rand_idx_val(sorted_long_data)
    print(log)
    assert binary_search(val, sorted_long_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_not_found)
def test_bs_not_found(sorted_med_data):
    val = sorted_med_data[-1] + random.randrange(1, 50)
    assert binary_search(val, sorted_med_data) == -1

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_one)
def test_bs_len_one():
    arr = [random.randrange(1, 50)]
    assert binary_search(0, arr) == -1
    assert binary_search(arr[0], arr) == 0

'''recursive '''

@pytest.mark.binary
@pytest.mark.repeat(repeat_short)
def test_bsr_short(sorted_short_data):
    idx, val, log = rand_idx_val(sorted_short_data)
    print(log)
    assert binary_search_recursive(val, sorted_short_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_med)
def test_bsr_med(sorted_med_data):
    idx, val, log = rand_idx_val(sorted_med_data)
    print(log)
    assert binary_search_recursive(val, sorted_med_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_long)
def test_bsr_long(sorted_long_data):
    idx, val, log = rand_idx_val(sorted_long_data)
    print(log)
    assert binary_search_recursive(val, sorted_long_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_not_found)
def test_bsr_not_found(sorted_med_data):
    val = sorted_med_data[-1] + random.randrange(1, 50)
    print(f"Generated value not in arr: {val}")
    '''
    # To debug use:
    breakpoint()
    result = binary_search_recursive(val, sorted_med_data)
    '''
    assert binary_search_recursive(val, sorted_med_data) == -1

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_one)
def test_bsr_len_one():
    arr = [random.randrange(1, 50)]
    assert binary_search_recursive(0, arr) == -1
    assert binary_search_recursive(arr[0], arr) == 0
