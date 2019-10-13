#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def sum_list(in_list):
    #this function adds up all the numbers in a list and returns sum
    total = 0
    for num in in_list:
        total += num
    return total

def cumulative_sum(in_list):
    #this function takes a list of numbers and returns the cumulative sum
    sum = [0] * len(in_list)
    for i in range(len(in_list)):
        sum[i] = sum_list(in_list[:i+1])
    return sum

if __name__ == "__main__":
    in_list = [1,2,3,4,5,6,7,8,9,10]
    print cumulative_sum(in_list)