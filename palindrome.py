#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def is_palindrome(word):
    #this function is a palindrome 
    #A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”.
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome_custom():
    word = raw_input('please enter a word: ')
    print is_palindrome(word)

def is_palindrome1(word):
    #the same with function palindrome 
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1

    return True

if __name__ == "__main__":
    print is_palindrome(' ')
    print is_palindrome('pop')
    print is_palindrome('moom')
    print is_palindrome('redivider')
    print is_palindrome1(' ')
    print is_palindrome1('pop')
    print is_palindrome1('moom')
    print is_palindrome1('redivider')
    is_palindrome_custom()
