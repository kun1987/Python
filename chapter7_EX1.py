#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:30:58 2019

@author: fengtian
"""

def countdown(n):
    #recursion countdown
    if not isinstance(n, int):
        print 'countdown is only defined for integers.'
        return None   
    elif n < 0:
        print 'countdown is not defined for negative integers.'
        return None
    else:
        if n <= 0:
            print 'Blastoff!'
        else:
            print n
            countdown(n-1)
            
def print_n(n):
    #iteration countdown
    if not isinstance(n, int):
        print 'print_n is only defined for integers.'
        return None   
    elif n < 0:
        print 'print_n is not defined for negative integers.'
        return None
    else:     
        while n > 0:
            print n
            n -= 1
        print 'Blastoff!'  

if __name__ == "__main__":
    print 'countdown(5):'
    countdown(5)
    print '\n'
    print 'print_n(5):'
    print_n(5)