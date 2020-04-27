from pytest import fixture, mark

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


@fixture
def get_number():
    return 6


def test_3(get_number):
    assert fib_iterative(get_number) == fib_cache(get_number)


@mark.parametrize('n, output', [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_4(n, output):
    assert fib_cache(n) == output


@mark.xfail
def test_5():
    assert fib_cache(1) == 0


@mark.skip(reason='very large number for brute force')
def test_6():
    assert fib_brute_force(40)
