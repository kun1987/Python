#!/usr/bin/env python2
# -*- coding: utf-8 -*-
known = {0:0, 1:1}

def fibonacci(n):
    #this is a fibonacci function
    #known is a dictionary that keeps track of the Fibonacci numbers we already know. It starts with two items: 0 maps to 0 and 1 maps to 1.
    '''
    Whenever fibonacci is called, it checks known. 
    If the result is already there, it can return immediately. 
    Otherwise it has to compute the new value,
    add it to the dictionary, and return it.
    '''
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    print known
    return res

if __name__ == '__main__':
    print fibonacci(6)