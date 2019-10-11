#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:50:41 2019

@author: Kun Wang
"""
import math

def hypotenus(a,b):
    #this function returns the length of the hypotenuse of a right triangle 
    #given the lengths of the two legs as arguments. 
    c = math.sqrt(a**2+b**2)
    return c
def hypotenus_custom():
    a = input('please enter a: ')
    b = input('please enter b: ')
    return hypotenus(a,b)

if __name__ == "__main__":	
    print hypotenus_custom()