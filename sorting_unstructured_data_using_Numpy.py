# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:36:09 2020

@author: HP
"""

import numpy as np
empdetails = [(101,18,20000),
     (102,27,10000),
     (100, 20, 15000)]
userdeftype = [("empid",int),
               ("empage",int),
               ("esal", float)]

empdata = np.array(empdetails, dtype = userdeftype)
print(empdata)
for data in empdata:
    print(data)
print("After sorting")
new_emp_data = np.sort(empdata,order = "empid")
print(new_emp_data)
print()
for data in new_emp_data:
    print(data)
              
    
