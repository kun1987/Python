#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def gcd(a,b):
    #this functon finds the greatest common divisor (GCD) of a and b.
    if a == 0 or b == 0:
        return 0
    elif not isinstance(a, int) or not isinstance(b, int):
        print 'gcd is only defined for integers.'
    else:     
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b,r)