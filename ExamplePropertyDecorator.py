# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:58:10 2020

@author: HP
"""

# example of property decorator

class book:
    def __init__(self):
        self.__bookName = ""
#@property defines getter method
    @property   
    def name(self):
        return self.__bookName
#@name.setter defines setter method
    @name.setter
    def name(self, names):
        self.__bookName = names
        
b = book()
# calling setter method
b.name = "algorithms in data structure"
# calling getter method
msg = b.name
print(msg)

        
