# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:18:14 2019

@author: Athan
"""
import sqlite3

conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperOrigoTags\tags.db')
curr = conn.cursor()

def couttags():
    curr.execute("""INSERT INTO 'origoTags_tb' (tags) VALUES ('migráció');""")
    curr.execute("""SELECT * FROM 'origoTags_tb'""")
    myList = curr.fetchall()
    myCountlist = []
    myFinallist = []
    reallyfinallist = [['legkissebb',9999999]]
    j=0
    l=0
    
    for i in myList:
        if myCountlist.count(i)==0:
            myCountlist.append(i)
            myCountlist.append(1)
        else:
            myCountlist[myCountlist.index(i)+1] += 1
    while j < len(myCountlist):
        kuka=[myCountlist[j],myCountlist[j+1]]
        myFinallist.append(kuka)
        kuka = []
        j+=2
    for k in myFinallist:
        
        while l < len(reallyfinallist):
            if reallyfinallist[l][1]>k[1]:
                reallyfinallist.insert(l,k)
                l=len(reallyfinallist)
            else:
                l+=1
         
            
            
            
            
    print(reallyfinallist)
couttags()

#p='a'
 #   for j in myCountlist;:
  #     if isinstance(j, int):
           
    