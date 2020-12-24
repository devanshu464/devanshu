# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:39:43 2020

@author: HP
"""

import numpy as np
a = np.array([10,20,30,40])
b = np.array([50,60,70,80,90])
res = np.concatenate((a,b))
print(res)