# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:10:35 2018

@author: Kritika Mishra
"""

file = open('positive.txt', 'r') 
p=file.read()
positive=p.split('\n')
print(positive) 
file.close()
file = open('negative.txt', 'r') 
n=file.read()
negative=n.split('\n')
print(negative) 
file.close()