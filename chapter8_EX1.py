#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def letter_backward(str):
    #this function takes a string as an argument and displays the letters backward, one per line.
    if len(str) == 0:
        print 'Over'
    else:
        for i in range(len(str)):
            print str[-i-1]

if __name__ == "__main__":
    print 'backward("apple")'
    letter_backward('apple')
    print'\n','backward('')'
    letter_backward('')
    print'\n','backward("a")'
    letter_backward('a')
