# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:04:09 2020

@author: HP
"""
def binarySearchAppr (arr, start, end, x):

   if end >= start:
      mid = start + (end- start)//2
      
      if arr[mid] == x:
          return mid
      
      elif arr[mid] > x:
             return binarySearchAppr(arr, start, mid-1, x)
      
      else:
          return binarySearchAppr(arr, mid+1, end, x)
   else:
      
      return -1
arr = sorted([10,1,2,11,23,21])
print("sorted list", arr)
x =2
result = binarySearchAppr(arr, 0, len(arr)-1, x)
if result != -1:
   print ("Element is present at index "+str(result))
else:
   print ("Element is not present in array")