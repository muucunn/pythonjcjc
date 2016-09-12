# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:51:05 2016

@author: zoumucheng
"""

class Person:
    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def greet(self):
        print ('Hello,world!I'm %s.'%self.name)
        