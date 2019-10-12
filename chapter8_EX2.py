#!/usr/bin/env python2
# -*- coding: utf-8 -*-

prefixes = 'JKLMNOPQ'
for letter in prefixes:
    #In Robert McCloskey’s book Make Way for Ducklings, 
    #the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'    
    print letter + suffix