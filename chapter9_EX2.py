#!/usr/bin/env python2
# -*- coding: utf-8 -*-

fin = open('words.txt')
def has_no_e(txt): 
    #this function prints only the words that have no “e” and computes the percentage of the words in the list have no “e.”
    count1 = 0 #count numbers of words with 'e'
    count2 = 0 #count numbers of words with no 'e'
    for line in txt:
    	word = line.strip()
    	if 'e' in word:
            count1 += 1
        else:
            print word
            count2 += 1
    percent = count2*1.0/(count1+count2)*100
    if count2 != 0:
        return percent
    else:
        return True
    
fin = open('words.txt')

if __name__ == "__main__":
    print str(has_no_e(fin)) + "% of the words don't have an 'e'."