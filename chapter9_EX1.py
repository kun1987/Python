#!/usr/bin/env python2
# -*- coding: utf-8 -*-

fin = open('words.txt')
for line in fin:
	word = line.strip()
	if len(word) > 20:
		print (word)