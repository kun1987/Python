#!/usr/bin/env python2

def print_hist(h):
    d = []
    d += sorted(h.keys())
    for c in d:
        print(c, h[c])
        

if __name__ == '__main__':
    v = {'p' : 1, 'a' : 1, 'r' : 2, 'o' : 1, 't' : 1}
    print print_hist(v)