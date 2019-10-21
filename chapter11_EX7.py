#!/usr/bin/env python2


def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
#        print m,n
#        print cache[m, n]
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
#        print cache[m, n]
        return cache[m, n]
    
if __name__ == '__main__':    
    cache = {}
    print ackermann(2, 3)