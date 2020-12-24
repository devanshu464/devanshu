# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:01:27 2020

@author: HP
"""

import numpy as np
a = np.array([[10,20,30],[40,50,60]])
b = np.array([[70,80,90],[100,110,120]])
res = np.concatenate((a,b))
print(res)
print()


res1 = np.concatenate((a,b), axis = 1)
print(res1)
print()

res2 = np.concatenate((a,b), axis= 0)
print(res2)