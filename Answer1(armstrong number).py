# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:09:19 2020

@author: HP
"""

num = int(input ("Enter an armstrong number\t"))
tempv = num
sum = 0

while tempv > 0:
    digit = tempv % 10
    sum = sum + digit**3
    tempv = tempv // 10
#print(sum)

if sum == num:
    print("Armstrong number")
else:
    print("not an armstrong number")