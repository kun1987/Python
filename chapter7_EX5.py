#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math
import sys

def factorial(n):
    #Computes factorial of n.
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        
        if abs(term) < 1e-15: break
        k += 1

    return 1 / total

def test_pi():
    #test pi with build-in function math.pi
    if abs(math.pi-estimate_pi()) < sys.float_info.epsilon:
        return True
    else:
        return False

if __name__ == "__main__":
    print estimate_pi()
    print test_pi()