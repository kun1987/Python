#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def capitalize_all(string):
    #this function uppers a string
    return string.upper()

def capitalize_nested(in_list):
    #this function takes a nested list of strings and returns a new nested list with all strings capitalized.
    for i in range(len(in_list)):
        if isinstance(in_list[i],str):
            in_list[i] = capitalize_all(in_list[i])
        else:
            capitalize_nested(in_list[i])
    return in_list

if __name__ == "__main__":
    in_list =[[[[['a','b','c','d'],'e','f','g'],'h','i','j'],'k','l','m'],'nop']
    print capitalize_nested(in_list)