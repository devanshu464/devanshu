# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:50:24 2020

@author: HP
"""

original_string = "Devanshu"
reverse_string = ""

i = len(original_string) - 1

while i >= 0:
    reverse_string = reverse_string + original_string[i]
    i = i - 1
print(reverse_string)