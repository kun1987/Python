#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 02:15:53 2019

@author: fengtian
"""

def is_between(x,y,z):
    #this is a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.
    if x < y < z:
        return True
    else:
        return False

if __name__ == "__main__":
    print is_between(2,3,4)  
    
    