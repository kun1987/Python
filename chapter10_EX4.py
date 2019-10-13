#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def middle(list):
    #this function takes a list and returns a new list that contains all but the first and last elements.
    del list[0]
    del list[-1]
    return list

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9]
    print middle(list)