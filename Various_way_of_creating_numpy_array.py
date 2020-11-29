# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:02:18 2020

@author: HP
"""

import numpy as np
l = [1,2,3,4,5]

a = np.array(l)
print(a)

l1 = range(100)
a1 = np.array(l1)
a2 = np.arange(100)
print(a)
print(a1)
print(a2)

a3 = np.arange(10,40)
print(a3)

a3 = np.arange(10,40,5)
print(a3)

a4 = np.linspace(0.2,0.3)
print(a4)

a5 = np.linspace(0.2,0.3,5)
print(a5)

b = np.zeros(3)
print(b)

c = np.zeros((3,3,))
print(c)

d = np.ones(3)
print(d)

d = np.ones((3,3))
print(d)

e = np.eye(4)
print(e)

f = np.diag([1,2,3,4])
print(f)

