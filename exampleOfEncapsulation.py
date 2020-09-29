# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 02:19:52 2020

@author: HP
"""

'''PILLARS OF PYTHON'''
'''ENCAPSULATION ; PROCESS OF PROVIDING CONTROL ACCESS TO THE'''
'''PRIVATE DATA MEMBERS OF A CLASS AND IT IS ACHIEVED BY'''
'''USING SETTERS AND GETTERS METHODS . DATA BINDING AND NOT DATA HIDING'''

class Book:
    
    def __init__(self, values):
        self.__pages = values
        
    def SETTERS(self,values):
        if values >= 1:
            self.__pages = values
            
    def GETTERS(self):
        return self.__pages
    
b = Book(100)

num = b.SETTERS(110)

print(b.GETTERS())
