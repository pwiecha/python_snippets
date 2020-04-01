'''Utilities to e.g. time algorithms'''

import functools
import time

def time_this(func):
    @functools.wraps(func)
    def time_this_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        #print(f"Func {func.__name__} took {run_time:.8f}")
        return value, run_time
    return time_this_wrapper
