# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:10:58 2020

@author: HP
"""

''' closure in python
we can invoke inner function present in nested function by returning
an address of an inner function '''

def outer():
    print("outer function")
    
    def inner():
        print("Inner function")
        
    return inner


ref1 = outer()


print(ref1)

ref1()

