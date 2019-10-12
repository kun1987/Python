#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def any_lowercase1(s):
    #check the first letter is a lowercase
    for c in s:
        print c
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    # chack 'c' is lowercase. since 'c' is a lowercase, return True,and break
    for c in s:
        print 'c'
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    # check every letter is lowercase, return the last one 
    for c in s:
        flag = c.islower()
        print flag
    return flag

def any_lowercase4(s):
    #return the last letter checking result.
    #once flag get a true value in the loop, the flag will keep true in the rest loop
    flag = False
    for c in s:
        print flag
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    #once the letter is not lower, return False and break the function
    for c in s:
        print c
        if not c.islower():
            return False
    return True

if __name__ == "__main__":
    print any_lowercase1('Exercise 11 ')
    print '\n'
    print any_lowercase2('Exercise 11 ')
    print '\n'
    print any_lowercase3('Exercise 11 ')
    print '\n'
    print any_lowercase4('Exercise 11 ')
    print '\n'
    print any_lowercase5('ereExercise 11 ')