# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:56:30 2019

@author: Athan
"""

import sqlite3
conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraper\url.db')
curr = conn.cursor()

def wordfreqencies():
    url=[]
    curr.execute("""SELECT url FROM 'origoUrl_tb';""")
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        url.append(urlrow)

           
wordfreqencies()