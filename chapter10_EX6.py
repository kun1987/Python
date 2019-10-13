#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def is_sorted(t):
    """takes a list as a parameter and returns True if the list is sorted in 
    ascending order and False otherwise."""
    t = input_t()
    for i in range(len(t)-1):  
        if t[i] > t[i+1]:
            return False
    return True
        

def input_t():
    """this function prompt custom to input a string and return the string of the list"""
    chr = raw_input('Enter a string: \n')
    t = list(chr)
    return t 

if __name__ == "__main__":
    print is_sorted(t)