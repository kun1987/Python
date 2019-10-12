#!/usr/bin/env python2
# -*- coding: utf-8 -*-
fin = open('words.txt')

def uses_only(words,letters):
    for line in words:
        word  = line.strip()
        if word == letters:
            return True
    return False
        
if __name__ == "__main__":
    print uses_only(fin,'aals')
        