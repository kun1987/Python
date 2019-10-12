#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def count(word,counting_letter,start):
    #this function counts the number of times a given letter appears in a word
    #start is the start letter of the traversing
    count = 0
    for letter in word[start:]:
        if letter == counting_letter:
            count = count + 1
    return count

if __name__ == "__main__":
    print count('Encapsulate this code in a function named count','t',20)

