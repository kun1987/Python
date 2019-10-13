#!/usr/bin/env python2
# -*- coding: utf-8 -*-

def are_reversed(dau, mom):
    """ this function return True if daughter and mom's ages, written as strings,
    are the reverse of each other"""
    
    """str..zfill:return the integer (i) written as a string with at least
    (len) digits"""
    dau_age = str(dau).zfill(len(str(dau)))
    mom_age = str(mom).zfill(len(str(dau)))
    if dau_age == mom_age[::-1]:
        return True

def count(diff):
    """this function returns the number of times the mother and daughter have pallindromic ages in their lives, 
    given the difference in age."""
    dau = 0
    count = 0
    while True:
        mom = dau + diff
        if are_reversed(dau, mom) or are_reversed(dau, mom+1):
            count = count + 1
            print dau, mom
        if mom > 120:
            break
        dau = dau + 1
    return count

def diff():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 18
    while diff < 70:
        n = count(diff)
        if n > 0:
            print'diff, num'
            print diff, n
            print' \n\n'
        diff = diff + 1

if __name__ == "__main__":
#    print are_reversed(24, 42)
#    print 'daughter  mother'
#    print  count(18)
    diff()