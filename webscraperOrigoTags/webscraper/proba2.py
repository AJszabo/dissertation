# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:49:30 2019

@author: Athan
"""
from collections import Counter
import sqlite3
conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
curr = conn.cursor()

def wordfreqencies():
    curr.execute("""SELECT tags FROM 'indexArticle_tb';""")
    tags1 = curr.fetchall()
    tag = []
    for tags in tags1:
        tags = str(tags)
        tags = tags.replace('(',"")
        tags = tags.replace(')',"")
        tags = tags.replace("'","")
        tags = tags.replace(',',"")
        tag += tags.split()
           
    print("Index:")
    print(Counter(tag).most_common(60))
    curr.execute("""SELECT tags FROM 'origoTags_tb';""")
    test = curr.fetchall()
    print("origo:")
    print(Counter(test).most_common(60))
    curr.execute("""SELECT tags FROM 'hvgArticle_tb';""")
    tags1 = curr.fetchall()
    tag = []
    for tags in tags1:
        tags = str(tags)
        tags = tags.replace('(',"")
        tags = tags.replace(')',"")
        tags = tags.replace("'","")
        tags = tags.replace(',',"")
        tag += tags.split()
           
    print("hvg:")
    print(Counter(tag).most_common(60))
    curr.execute("""SELECT tags FROM 'negynegynegyArticle_tb';""")
    tags1 = curr.fetchall()
    tag = []
    for tags in tags1:
        tags = str(tags)
        tags = tags.replace('(',"")
        tags = tags.replace(')',"")
        tags = tags.replace("'","")
        tags = tags.replace(',',"")
        tag += tags.split()
           
    print("444:")
    print(Counter(tag).most_common(60))
#    curr.execute("""SELECT tags FROM 'negynegynegyArticle_tb';""")
#    tags1 = curr.fetchall()
#    tag = []
#    for tags in tags1:
#        tags = str(tags)
#        tags = tags.replace('(',"")
#        tags = tags.replace(')',"")
#        tags = tags.replace("'","")
#        tags = tags.replace(',',"")
#        tag += tags.split()
#           
#    print("Index:")
#    print(Counter(tag).most_common(60))

    
wordfreqencies()
