# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:18:45 2020

@author: HP
"""

'''3x+2y+7z = 3
   5x+3y+2z = 5
   7x+6y+2z = 5
   '''
import numpy as np
a1 = np.array([[3,2,7],[5,3,2],[7,6,2]])
a2 = np.array([[3],[5],[5]])
res1 = np.linalg.solve(a1, a2)
print(res1)