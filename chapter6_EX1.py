#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:34:48 2019

@author: Kun Wang
"""

def compare(x,y):
    #this function returns 1 if x > y, 0 if x == y, and -1 if x < y.
    if x > y:
        print 1
    elif x==y:
        print 0
    else: 
        print -1

def cpmpare_customs():
    x = input("Please input x: ")
    y = input("Please input y: ")
    return compare(x,y)

cpmpare_customs()  
    