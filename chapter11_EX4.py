#!/usr/bin/env python2
def reverse_lookup_wrong(d, v):
    #this functionthat takes a value and returns the first key that maps to that value
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_correct(d,v):
    #this function builds and returns a list of all keys that map to v !
    #or an empty list if there are none.
    t = list()
    for k in d:
        if d[k] == v:
            t.append(k)
    return t

if __name__ == '__main__':
    d = {'a': 1, 'o': 1, 'p': 1, 'r': 2, 't': 1}
    v = 3
#    print reverse_lookup_wrong(d, v)
    print reverse_lookup_correct(d, v)
