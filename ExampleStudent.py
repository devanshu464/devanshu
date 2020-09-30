# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:17:36 2020

@author: HP
"""

# student record details"

class Student:
    def __init__(self):
        self.__name = ""
        self.__usn = ""
        self.__course = ""
        self.__branch = ""
        
    def setter(self):
        print("Enter the names")
        names = input()
        print("Enter the university roll number")
        usns = input()
        print("Enter the courses")
        courses = input()
        print("Enter the branches")
        branches = input()
        
        
        self.__name = names
        self.__usn = usns
        self.__course = courses
        self.__branch = branches
        
    def getter(self):
        print("Name : {}\nusn : {}\ncourse : {}\nbranch : {}\n".format(self.__name,self.__usn,
                                                 self.__course,
                                                 self.__branch))
        
s = Student()


s.setter()
s.getter()
print("Do you want to add more records?\nREply with yes or no")
decision = input()
if(decision == "yes"):
    s.setter()
    s.getter()

#s2 = s.setter("Akriti", "1ew16cs067","BE","CSE")

#s.getter()



