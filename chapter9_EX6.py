#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def is_abecedarian(word):
    #this function returns True if the letters in a word appear in alphabetical order (double letters are ok)
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
			return False
    return True

def is_abecedarian1(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def is_abecedarian2(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian1(word[1:])

def is_abecedarian3(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

	
def count_abecedarian(word):
    #this function counts how many abecedarian words are there?
    for i in range(len(word)-1):
        new_word = word[:i+2]
        if is_abecedarian(new_word)==True:
           count = len(new_word)
        else:
           count = len(new_word)-1
           break
    return count
        
   
if __name__ == "__main__":
    print is_abecedarian('abefcedarian')
    print is_abecedarian1('abefcedarian')
    print is_abecedarian2('abefcedarian')
    print is_abecedarian3('abefcedarian')
    print count_abecedarian('abefcedarian')
