#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#from http : //thinkpython.com/code/wordlist.py。

import time

def make_word_list1(fin):
    """Reads lines from a file and builds a list using append."""
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2(fin):
    """Reads lines from a file and builds a list using list +."""
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t

if __name__ == "__main__":
    #.append takes longer time to run
    fin = open('words.txt')
    start_time = time.time()
    t = make_word_list1(fin)
    elapsed_time = time.time() - start_time
    
    print elapsed_time, 'seconds'
    
    start_time = time.time()
    t = make_word_list2(fin)
    elapsed_time = time.time() - start_time
    
    print elapsed_time, 'seconds'