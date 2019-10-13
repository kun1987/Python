#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# from: http://thinkpython.com/code/birthday.py.
import random

def has_duplicates(t):
    """this function takes a list and 
    returns True if there is any element that appears more than once."""
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_birthday(n):
    """this function generates random dsmples of birthdays, 
    numbers of students is its argument
    and returns a list of integers between 1 and 365, with length (n)."""
    t = []
    for i in range(n):
        birthday = random.randint(1, 365)
        t.append(birthday)
    return t


def count_matches(students, samples):
    """Generates (samples) samples of (students) students, and counts
    how many of them have at least one pair of students with the same bday."""
    count = 0
    for i in range(samples):
        t = random_birthday(students)
        if has_duplicates(t):
            count += 1
    return count

if __name__ == "__main__":
    """run the birthday simulation 1000 times and print the number of matches"""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)
    
    print 'After %d simulations' % num_simulations
    print 'with %d students' % num_students
    print 'there were %d simulations with at least one match' % count