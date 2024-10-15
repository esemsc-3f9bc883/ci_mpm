from functools import cache
import math

__all__ = ['my_sum', 'factorial', 'compute_sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


def compute_sin(x):
    return math.sin(x)
