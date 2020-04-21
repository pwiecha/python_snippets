''' decorators wrap a function, modifying its behavior'''
def base():
    print("Inside base function")

def basic_decorator(decorated_func):
    def basic_wrapper():
        print("Inside wrapper before calling the decorated func")
        decorated_func()
        print("Inside wrapper after calling the decorated func")
    return basic_wrapper

@basic_decorator
def base2():
    print("Inside base function")

def basic_decorator_args(decorated_func):
    def basic_args_wrapper(*args, **kwargs):
        print("Inside wrapper before calling the decorated func")
        decorated_func(*args, **kwargs)
        print("Inside wrapper after calling the decorated func")
    return basic_args_wrapper

@basic_decorator_args
def base_repeat(amount, sentence="Foo"):
    for i in range(amount):
        print(f"Hello {sentence}!")

from functools import wraps
def wraps_decorator_args(decorated_func):
    @wraps(decorated_func)
    def wraps_args_wrapper(*args, **kwargs):
        print("Inside wrapper before calling the decorated func")
        decorated_func(*args, **kwargs)
        print("Inside wrapper after calling the decorated func")
    return wraps_args_wrapper

@wraps_decorator_args
def another_repeat(amount, sentence="Foo"):
    for i in range(amount):
        print(f"Hello {sentence}!")


if __name__ == "__main__":
    print("Basic invocation")
    base()
    base = basic_decorator(base)
    print("Decorated")
    base()
    print("Decorated w/ syntactic sugar")
    base2()
    print("Passing args")
    base_repeat(3, sentence = 'Bar')

    print("\nDecorated functions will have their name replaced / masked "
          "with the decorator function name")
    print(f"Decorated base_repeat() name: {base_repeat.__name__}")
    print("\nFunctools wraps solves this problem")
    another_repeat(3, sentence='Rab')
    print(f"Decorated another_repeat() name: {another_repeat.__name__}")
    print(f"Works on func doc too obviously")