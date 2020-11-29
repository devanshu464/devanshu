# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:36:29 2020

@author: HP
"""

string = "a5b6c7d2"

for i in range(0,len(string),2):
    print(string[i]*int(string[i+1]),end = "")
    
    
    
