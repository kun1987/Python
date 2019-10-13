#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def remove_duplicates(org_list):
    """that takes a list and returns a new list with only the unique elements 
    from the original."""
    t = []
    for element in org_list:
        if element not in t:
            t.append(element)
    return t
if __name__ == "__main__":
    print(remove_duplicates(['apple', 'pare', 'apple', 'banana', 'apple']))