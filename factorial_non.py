#!/user/bin/env python

from nose.tools import assert_equal


def factorial_nonrecursive(n):
    if n == 0:
        result = 1
    else:
        result = 1
        i = 1
        while i < (n + 1):
            result *= i
            i += 1
    return result


def test_factorial():
    assert_equal(factorial_nonrecursive(1), 1)
    assert_equal(factorial_nonrecursive(0), 1)
    assert_equal(factorial_nonrecursive(5), 120)
    # TODO: add more


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_nonrecursive(int(nconditions))
    print("Number of possible trial orders: " + str(norders))
