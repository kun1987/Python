#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def nested_sum(in_list):
    #this function takes a nested list of integers and add up the elements from all of the nested lists
    total = 0
    for item in in_list:
        if isinstance(item,type(list)):
            total += nested_sum(item)
        else:
            total += item
    return total

if __name__ == "__main__":
    in_list =[[[[[1,2,3,4],4,5,6],3,4,5],2,3,4],1,2,3] #sum=52
    print nested_sum(in_list)