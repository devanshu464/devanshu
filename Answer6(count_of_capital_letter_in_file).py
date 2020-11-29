# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 07:57:33 2020

@author: HP
"""
count = 0
fptr = open("Answer2.txt", "r")
data = fptr.read()
#print(data)
for i in data:
    if i.isupper():
        count = count + 1
print(count)