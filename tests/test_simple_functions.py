import pytest
import math

from simple_functions import my_sum, factorial, compute_sin


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('x, expected', [
        (0, 0),
        (math.pi / 2, 1),
        (math.pi, 0),
        (3 * math.pi / 2, -1),
        (2 * math.pi, 0),
    ])
    def test_compute_sin(self, x, expected):
        assert math.isclose(compute_sin(x), expected, rel_tol=1e-9, abs_tol=1e-9), f"Failed for x={x}"
