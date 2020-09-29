# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:42:23 2020

@author: HP
"""

'''Decorators in python'''

''' when we pass function as an argument to outer function and '''
''' returning the address of inner function then it is referred
decorator'''

'''the below is showing the example of decorator but its not proper example'''

def print_mssg():
    print("hi, devanshu")
    
def outer(print1):
    print("outer collected the address")
    
    def inner():
        print("Entering inner")
        ref1 = print1
        ref1()
        print("leaving inner")
    return inner

ptr1 = print_mssg


ptr2 = outer(ptr1)

ptr2()

print("program completed")