# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:17:01 2020

@author: HP
"""
import numpy as np
l = [[10,20,30],[1,2,3]]
a = np.array(l)
print(a)

print(a.shape)
a.shape = (3,2)
print(a.shape)
#a.shape = (3,3)
print(a)


#reshape

l1 = [[10,20,30],[40,50,60]]
b = np.array(l1)
print(b)
#b.reshape = (3,2)
c = b.reshape(3,2)
print(c)

#d = b.reshape(3,3)
#print(d)

#resize

l2 = [[10,15,20], [21,22,23]]
e = np.array(l2)
print(e)
#e.resize = (3,2)
#np.resize = (3,2)
#print(e)
e.resize(3,2)
print(e)


f = np.resize(e ,(3,2))
print(f)
