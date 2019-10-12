#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import math

def square_root(a):
    #this function computes square roots with Newton’s method
    x = 3.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < sys.float_info.epsilon:
            break
        x = y
    return x

def test_square_root():
    for i in range(1,10):
        print('{:<2.1f}{:>13}{:^13}'.format(i,math.sqrt(i),square_root(i))),abs(math.sqrt(i)-square_root(i))
if __name__ == "__main__":
    test_square_root()