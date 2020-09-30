# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:07:59 2020

@author: HP
"""

# Uses of Property function in python

class Person:
    def __init__(self):
        self.__name = ""
        self.__location = ""
        self.__contact = ""
        
    def setter(self,names):
        
        print("setter is called")
        
        self.__name = names
        
    def getter(self):
        print(" getter is called")
        print("Name : {}\n"
              .format(self.__name))
        
    getset = property(getter,setter)
p = Person()
p.getset = "Devanshu"
msg = p.getset

#p.setter()
#p.getter()

        

 