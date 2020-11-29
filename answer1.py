# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 08:35:40 2020

@author: HP
"""

"cumulative sum"

def cumulative_sum(list1):
    cum_list = []
    sum = 0
    j = 0
    for i in range(len(list1)):
        
        sum = sum + list1[j]
        j = i + 1
        cum_list.append(sum)
    print("cumulative sum of a list is:", end = " ")
    print( cum_list)
    
#Driver code
list1 = [10,20,30,40,50]
cumulative_sum(list1)

        