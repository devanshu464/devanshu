# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 08:32:12 2020

@author: HP
"""

def Interpolation_search(list1, low, high, ele_search):
    if (low <= high and ele_search >= list1[low] and ele_search <= list1[high] ):
        pos = low + ((high - low) // (list1[high] - list1[low]) *(ele_search - list1[low]))
        
        if list1[pos] == ele_search:
            return pos
        elif list1[pos] < ele_search:
            return Interpolation_search(list1, pos + 1, high, ele_search)
        elif list1[pos] > ele_search:
            return Interpolation_search(list1, low, pos - 1, ele_search)
        
    else:
        return -1
    
arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
 
# Element to be searched
x = 12
index = Interpolation_search(arr, 0, n - 1, x)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")