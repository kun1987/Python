#!/usr/bin/env python2
# -*- coding: utf-8 -*-

fin = open('words.txt')

def uses_all(words, letters):
    for letter in words: 
        if letter not in letters:
            return False
        return True

if __name__ == "__main__":
    print uses_all('abcdefg', 'acd')