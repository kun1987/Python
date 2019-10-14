#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def get_dict():
    #this function reads the words in words.txt and stores them as keys in a dictionary
    #the values are None.
	t = []
	fin = open("words.txt")
	for line in fin:
		word = line.strip()
		t.append(word)
	d = dict.fromkeys(t)
	return d
	
def search_dict(d, s):
    #this function checks whether a string is in the dictionary.
	if s in d:
		return True
	else:
		return False
		

if __name__ == '__main__':
	d = get_dict()
	print search_dict(d, "aalsf")
