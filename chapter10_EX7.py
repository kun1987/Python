#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def check(s1, s2): 
    """function to check if two strings are anagram or not  
    it takes two strings and returns True if they are anagrams."""
    if(sorted(s1)== sorted(s2)): 
        return True
    else: 
        return False         
          
if __name__ == "__main__":
    s1 ="python"
    s2 ="onthpy" 
    s3 ="onthpe"
    print check(s1, s2) 
    print check(s1, s3) 