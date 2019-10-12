#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def find(word, letter,start):
    #this function search the position of letter in a word
    #format:find('word', 'letter',start)
    #start is the index in word where it should start looking
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
if __name__ == "__main__":
    print find('Modify find so that it has a third parameter, the index in word where it should start looking', 'g',10)