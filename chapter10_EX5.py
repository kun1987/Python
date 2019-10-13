#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def chop(list):
    #this function takes a list, modifies it by removing the first and last elements, and returns None.
    del list[0]
    del list[-1]
    

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9]
    print chop(list)