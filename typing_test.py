# -*- coding: utf-8 -*-

"""
Example usage of python type hints
"""


def greeting(name: str) -> str:
    return 'Hello ' + name


# PEP 484:  when an argument is annotated as having type float,
# an argument of type int is acceptable
def sum_two(first_arg: float, second_arg: float) -> float:
    return first_arg + second_arg


if __name__ == "__main__":
    greeting("Pawel")
    greeting(5)
    greeting(['foo', 'bar'])

    sum_two(5, 5.1)
    sum_two('a', 'b')
    sum_two({'a': 5}, {4: 'bar'})
