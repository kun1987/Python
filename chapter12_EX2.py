#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def sort_by_length(words):
    '''
    this function extracts the sorted elements of the sequence
    The first loop builds a list of tuples, where each tuple is a word preceded by its length.

    sort compares the first element, length, first, and only considers the second element to break ties. 
    The keyword argument reverse=True tells sort to go in decreasing order.

    The second loop traverses the list of tuples and builds a list of words in descending order of length.
    '''
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)
    print t

    res = []
    for length, word in t:
        res.append(word)
    return res


if __name__ == '__main__':   
     words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']
     print sort_by_length(words)