#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    """
    if not isinstance(m, int) or not isinstance(n, int):
        print 'Ackermann is only defined for integers.'
        return None
    elif m < 0 or n < 0:
        print 'Ackermann is not defined for negative integers.'
        return None
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))
if __name__ == "__main__":
    #The recursion limit is usually 1000
    #if calculate ackermann(5,4), the program interrapt and prompt( RuntimeError: maximum recursion depth exceeded)
    print ackermann(2,4.2)
    print ackermann(-2,4)
    print ackermann(2,4)
