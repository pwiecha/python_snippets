''' decorators wrap a function, modifying its behavior'''
def base():
    print("Inside base function")

def basic_decorator(decorated_func):
    def wrapper():
        print("Inside wrapper before calling the decorated func")
        decorated_func()
        print("Inside wrapper after calling the decorated func")
    return wrapper

@basic_decorator
def base2():
    print("Inside base function")

def basic_decorator_args(decorated_func):
    def wrapper(*args, **kwargs):
        print("Inside wrapper before calling the decorated func")
        decorated_func(*args, **kwargs)
        print("Inside wrapper after calling the decorated func")
    return wrapper

@basic_decorator_args
def base_repeat(amount, sentence="Foo"):
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