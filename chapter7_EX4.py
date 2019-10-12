#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
def eval_loop():
    #this function iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.
    while True:
        myinput = raw_input('Enter >>>')
        if myinput == 'done':
            break      
        print eval(myinput)
    print 'Done'
    
if __name__ == "__main__":
    eval_loop()