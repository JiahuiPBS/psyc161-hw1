#!/user/bin/env python

import time

def factorial_recursive(n):
        if n == 0:
            return 1
        else:
            return n * factorial_recursive(n-1)
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
        
        
def comp_time(m):
    startf = time.clock()
    i = 1
    while i < 10001:
        factorial_recursive(m)
        i += 1
    elapsedf = time.clock() - startf

    startfn = time.clock()
    j = 1
    while j < 10001:
        factorial_nonrecursive(m)
        j += 1
    elapsedfn = time.clock() - startfn

    ratio = elapsedf/elapsedfn
    return ratio

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    import matplotlib.pyplot as pl
    tratios = []
    ns = range(10, 85, 5)
    for n in ns:
        tratio = comp_time(n)
        tratios.append(tratio)
    pl.plot(ns, tratios)
    pl.show()

