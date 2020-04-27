from pytest import mark

from development.math import fib_brute_force, fib_cache, fib_iterative


@mark.small
def test_1():
    assert fib_brute_force(1) == 1
    assert fib_cache(1) == 1
    assert fib_iterative(1) == 1


@mark.large
def test_2():
    for i in range(15):
        output = {fib_iterative(i), fib_cache(i), fib_brute_force(i)}

        assert len(output) == 1
