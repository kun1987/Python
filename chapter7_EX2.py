#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys

def square_root(a):
    #this function computes square roots with Newton’s method
    x = 3.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < sys.float_info.epsilon:
            break
        x = y
    return x

if __name__ == "__main__":
    print square_root(4)
    print square_root(2)