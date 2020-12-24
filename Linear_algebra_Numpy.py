# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:12:36 2020

@author: HP
"""

import numpy as np
a = np.array([[1,2],[3,4]])
res1 = np.linalg.inv(a)#inverse_matrix
print(res1)
print()
res2 = np.linalg.matrix_power(a, 2)
print(res2)
print()
res3 = np.linalg.matrix_power(a,0)#identity matrix
print(res3)
print()
res4 = np.linalg.matrix_power(a, -1)#inverse matrix
print(res4)