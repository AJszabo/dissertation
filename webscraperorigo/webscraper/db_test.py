# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:09:51 2019

@author: Athan
"""
import sqlite3

conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraper\url.db')
curr=conn.cursor()

def read_from_db():
        curr.execute("SELECT tags FROM 'origoUrl_tb';")
        for row in curr.fetchall():
            print(row)
            
            
            
read_from_db()