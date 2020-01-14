# -*- coding: utf-8 -*-

"""
Example usage of python type hints
"""


def greeting(name: str) -> str:
    return 'Hello ' + name


def no_return_type() -> None:
    return

# PEP 484:  when an argument is annotated as having type float,
# an argument of type int is acceptable
# Also, how to mix type with default argument value
def arith_op(first_arg: float, second_arg: float, op: str = 'add') -> float:
    return first_arg + second_arg if op == 'add' else first_arg - second_arg

# TODO list, tuples, dicts, classes and custom types + typing before assigning a value

if __name__ == "__main__":
    # passing
    greeting("Pawel")

    arith_op(5, 5.1, 'add')
    arith_op(10, 3.5, 'sub')

    no_return_type()

    # failing
    greeting(5)
    greeting(['foo', 'bar'])
    arith_op('a', 'b', 'c')
    arith_op({'a': 5}, {4: 'bar'})
    arith_op(10, 3.5, 3)
    no_return_type(5)
