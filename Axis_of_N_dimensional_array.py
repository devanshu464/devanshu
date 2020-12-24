# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:54:18 2020

@author: HP
"""
import numpy as np
l = [[16,99,50],[45,70,89],[115,95,150]]

a = np.array(l)
print(a)
print()
print(a.min())
print()
print(a.max())
print()
print(a.sum())
print()
print(a.mean())
print()
print(a.std())
print()
print(a.min(axis = 0))
print()
print(a.max(axis = 0))
print()
print(a.min(axis = 1))
print()
print(a.max(axis = 1))