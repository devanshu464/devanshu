# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:53:30 2020

@author: HP
"""

'''correct decorator example using @'''


def outer(ptr1):
    print("outer function")
    
    def inner():
        ref1 = ptr1
        print("calling another function")
        ref1()
        print("inner function ends")
    return inner


@outer

def print_mssg():
    print("Good morning, Devanshu")

print_mssg()