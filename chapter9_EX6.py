#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def is_abecedarian(word):
    #this function returns True if the letters in a word appear in alphabetical order (double letters are ok)
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
			return False
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
    print count_abecedarian('abefcedarian')
