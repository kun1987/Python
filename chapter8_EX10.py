#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def is_palindrome(word):
    #this function is a palindrome 
    #A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”.
    if len(word) <= 1:
        return True
    if word[::1]== word[::-1]:
        return True
    return False

if __name__ == "__main__":
    print is_palindrome(' ')
    print is_palindrome('pop')
    print is_palindrome('moom')
    print is_palindrome('redivider')