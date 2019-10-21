#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def histogram(s):
    d = dict.fromkeys(s)
    for chr in s:
        d[chr] = s.count(chr)
    return d


if __name__ == "__main__":	
    s = 'applepearorange'
    print histogram(s)
