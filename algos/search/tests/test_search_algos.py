import pytest
import random
from ..src.linear_search import linear_search
from ..src.binary_search import binary_search
from ..src.binary_search import binary_search_recursive
from ..src.binary_search import binary_search_recursive_two

@pytest.fixture
def sorted_short_data():
    return list(range(-1000,1001))

@pytest.fixture
def sorted_med_data():
    return list(range(-10000,10001))

@pytest.fixture
def sorted_long_data():
    return list(range(int(-1e5),int(1e5)))

def rand_idx_val(sequence):
    ''' Randomly select index and element from sequence '''
    idx = random.choice(range(len(sequence)))
    return idx, sequence[idx], f"Searching for idx: {idx} val: {sequence[idx]}"

# Pytest number or repetitions based on test type
repeat_not_found = 50
repeat_len_one = 50
repeat_len_two = 50
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
    val_above = sorted_med_data[-1] + random.randrange(1, 50)
    val_below = sorted_med_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    assert linear_search(val, sorted_med_data) == -1

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_one)
def test_ls_len_one():
    arr = [random.randrange(1,50)]
    assert linear_search(0, arr) == -1
    assert linear_search(arr[0], arr) == 0

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_two)
def test_ls_len_two():
    arr = random.sample(range(1,50), 2)
    assert linear_search(0, arr) == -1
    assert linear_search(arr[0], arr) == 0
    assert linear_search(arr[1], arr) == 1

@pytest.mark.linear
@pytest.mark.timing
def test_ls_expected_time(sorted_long_data, benchmark):
    idx, val, log = rand_idx_val(sorted_long_data)
    benchmark(linear_search, target=val, sequence=sorted_long_data)

@pytest.mark.linear
@pytest.mark.timing
def test_ls_worst_time(sorted_long_data, benchmark):
    val_above = sorted_long_data[-1] + random.randrange(1, 50)
    val_below = sorted_long_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    benchmark(linear_search, target=val, sequence=sorted_long_data)

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
    val_above = sorted_med_data[-1] + random.randrange(1, 50)
    val_below = sorted_med_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    assert binary_search(val, sorted_med_data) == -1

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_one)
def test_bs_len_one():
    arr = [random.randrange(1, 50)]
    assert binary_search(0, arr) == -1
    assert binary_search(arr[0], arr) == 0

@pytest.mark.linear
@pytest.mark.repeat(repeat_len_two)
def test_bs_len_two():
    arr = random.sample(range(1,50), 2)
    arr.sort()
    assert binary_search(0, arr) == -1
    assert binary_search(arr[0], arr) == 0
    assert binary_search(arr[1], arr) == 1

@pytest.mark.binary
@pytest.mark.timing
def test_bs_expected_time(sorted_long_data, benchmark):
    idx, val, log = rand_idx_val(sorted_long_data)
    benchmark(binary_search, target=val, sequence=sorted_long_data)

@pytest.mark.binary
@pytest.mark.timing
def test_bs_worst_time(sorted_long_data, benchmark):
    val_above = sorted_long_data[-1] + random.randrange(1, 50)
    val_below = sorted_long_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    benchmark(binary_search, target=val, sequence=sorted_long_data)

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
    val_above = sorted_med_data[-1] + random.randrange(1, 50)
    val_below = sorted_med_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    print(f"Generated value not in arr: {val}")
    assert binary_search_recursive(val, sorted_med_data) == -1

@pytest.mark.binary
@pytest.mark.repeat(repeat_len_one)
def test_bsr_len_one():
    arr = [random.randrange(1, 50)]
    assert binary_search_recursive(0, arr) == -1
    assert binary_search_recursive(arr[0], arr) == 0

@pytest.mark.binary
@pytest.mark.repeat(repeat_len_two)
def test_bsr_len_two():
    arr = random.sample(range(1,50), 2)
    arr.sort()
    assert binary_search_recursive(0, arr) == -1
    assert binary_search_recursive(arr[0], arr) == 0
    assert binary_search_recursive(arr[1], arr) == 1

@pytest.mark.binary
@pytest.mark.timing
def test_bsr_expected_time(sorted_long_data, benchmark):
    idx, val, log = rand_idx_val(sorted_long_data)
    benchmark(binary_search_recursive, target=val, sequence=sorted_long_data)

@pytest.mark.binary
@pytest.mark.timing
def test_bsr_worst_time(sorted_long_data, benchmark):
    val_above = sorted_long_data[-1] + random.randrange(1, 50)
    val_below = sorted_long_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    benchmark(binary_search_recursive, target=val, sequence=sorted_long_data)

'''recursive second version'''

@pytest.mark.binary
@pytest.mark.repeat(repeat_short)
def test_bsr_two_short(sorted_short_data):
    idx, val, log = rand_idx_val(sorted_short_data)
    print(log)
    assert binary_search_recursive_two(val, sorted_short_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_med)
def test_bsr_two_med(sorted_med_data):
    idx, val, log = rand_idx_val(sorted_med_data)
    print(log)
    assert binary_search_recursive_two(val, sorted_med_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_long)
def test_bsr_two_long(sorted_long_data):
    idx, val, log = rand_idx_val(sorted_long_data)
    print(log)
    assert binary_search_recursive_two(val, sorted_long_data) == idx

@pytest.mark.binary
@pytest.mark.repeat(repeat_not_found)
def test_bsr_two_not_found(sorted_med_data):
    val_above = sorted_med_data[-1] + random.randrange(1, 50)
    val_below = sorted_med_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    print(f"Generated value not in arr: {val}")
    assert binary_search_recursive_two(val, sorted_med_data) == -1

@pytest.mark.binary
@pytest.mark.repeat(repeat_len_one)
def test_bsr_two_len_one():
    arr = [random.randrange(1, 50)]
    assert binary_search_recursive_two(0, arr) == -1
    assert binary_search_recursive_two(arr[0], arr) == 0

@pytest.mark.binary
@pytest.mark.repeat(repeat_len_two)
def test_bsr_two_len_two():
    arr = random.sample(range(1,50), 2)
    arr.sort()
    assert binary_search_recursive_two(0, arr) == -1
    assert binary_search_recursive_two(arr[0], arr) == 0
    assert binary_search_recursive_two(arr[1], arr) == 1

@pytest.mark.binary
@pytest.mark.timing
def test_bsr_two_expected_time(sorted_long_data, benchmark):
    idx, val, log = rand_idx_val(sorted_long_data)
    benchmark(binary_search_recursive_two, target=val, sequence=sorted_long_data)

@pytest.mark.binary
@pytest.mark.timing
def test_bsr_two_worst_time(sorted_long_data, benchmark):
    val_above = sorted_long_data[-1] + random.randrange(1, 50)
    val_below = sorted_long_data[0] - random.randrange(1, 50)
    val = random.choice([val_above, val_below])
    benchmark(binary_search_recursive_two, target=val, sequence=sorted_long_data)
