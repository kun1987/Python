#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def is_power(a,b):
    #this function is a power of b
    if b == 0:
        print 'anynumber is not divisable by 0'
        return None 
    elif a == b:
        return True
    elif a % b == 0:
        return is_power(a/b,b)
    else:
        return False
def is_power_custom():
    a = int(raw_input('Please enter a: '))
    b = int(raw_input('Please enter b: '))
    print is_power(a,b)

if __name__ == "__main__":
    print is_power(8,2)
    is_power_custom()