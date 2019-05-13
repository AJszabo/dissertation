# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:18:14 2019

@author: Athan
"""

myList = ["a","a","d","b","e","c","a","d","c","b"]
myCountlist = []

for i in myList:
    if myCountlist.count(i)==0:
        myCountlist.append(i)
        myCountlist.append(1)
    else:
        myCountlist[myCountlist.index(i)+1] += 1

print(myCountlist)
