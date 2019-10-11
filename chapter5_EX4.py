#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:10:49 2019

@author: Kun Wang
"""
def is_triangle(a, b, c):
    #this function is for check is it able to arrange a triangle with three given sticks
    #formula:If any of the three lengths is greater than the sum of the other two, 
    #then you cannot form a triangle. 
    #therwise, you can. 
    #(If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)
	if a + b > c and a + c > b and b + c > a:
		return "Yes"
        if a + b == c or a + c == b or b + c == a:
            print "degenerate"
	else:
		return "No"
    
def is_triangle_custom():
	a = input("Please input a: ")
	b = input("Please input b: ")
	c = input("Please input c: ")
	return is_triangle(a, b, c)

if __name__ == "__main__":	
    #first test:
    print is_triangle(3, 4, 5)
	#second test:
    is_triangle_custom()
