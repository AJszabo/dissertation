# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:02:01 2019

@author: 1632715
"""
import sqlite3
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from langdetect import detect
from nltk.stem.snowball import SnowballStemmer


def get_tokens(text):
    tokens = word_tokenize(text)
    return [token.lower() for token in tokens]
    
def nlp():
    tagged_data = []
    stemmer = SnowballStemmer("hungarian")
    hu = detect("nagyon szertém ha működnél köszi puszi")
#   assert gensim.models.doc2vec.FAST_VERSION > -1
    conn = sqlite3.connect(r'C:\Users\Domos\Documents\andris disszertacio\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT DISTINCT paragaph FROM 'hvgArticle_tb' where start_url like "%/2014%";""")
    HVG14=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        if detect(urlrow)==hu:
            HVG14 += urlrow
    print("HVG14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'hvgArticle_tb' where start_url like "%/2015%";""")
    HVG15=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        if detect(urlrow)==hu:
            HVG15 += urlrow
    print("HVG15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'hvgArticle_tb' where start_url like "%/2016%";""")
    HVG16=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        if detect(urlrow)==hu:
            HVG16 += urlrow
    print("HVG16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'hvgArticle_tb' where start_url like "%/2017%";""")
    HVG17=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        if detect(urlrow)==hu:
            HVG17 += urlrow
    print("HVG17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'hvgArticle_tb' where start_url like "%/2018%";""")
    HVG18=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        if detect(urlrow)==hu:
            HVG18 += urlrow
    print("HVG18 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'huszonnegyhuArticle_tb' where start_url like "%/2014/%";""")
    huszonnegy14=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                huszonnegy14 += urlrow
    print("huszonnegy14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'huszonnegyhuArticle_tb' where start_url like "%/2015/%";""")
    huszonnegy15=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                huszonnegy15 += urlrow

    print("huszonnegy15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'huszonnegyhuArticle_tb' where start_url like "%/2016/%";""")
    huszonnegy16=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                huszonnegy16 += urlrow
    print("huszonnegy16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'huszonnegyhuArticle_tb' where start_url like "%/2017/%";""")
    huszonnegy17=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                huszonnegy17 += urlrow
    print("huszonnegy17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'huszonnegyhuArticle_tb' where start_url like "%/2018/%";""")
    huszonnegy18=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                huszonnegy18 += urlrow
    print("huszonnegy18 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'indexArticle_tb' where start_url like "%/2014/%";""")
    index14=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                index14 += urlrow
    print("index14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'indexArticle_tb' where start_url like "%/2015/%";""")
    index15=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                index15 += urlrow
    print("index15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'indexArticle_tb' where start_url like "%/2016/%";""")
    index16=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                index16 += urlrow
    print("index16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'indexArticle_tb' where start_url like "%/2017/%";""")
    index17=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                index17 += urlrow
    print("index17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'indexArticle_tb' where start_url like "%/2018/%";""")
    index18=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                index18 += urlrow
    print("index18 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'negynegynegyArticle_tb' where start_url like "%/2014/%";""")
    nnn14=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                nnn14 += urlrow
    print("nnn14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'negynegynegyArticle_tb' where start_url like "%/2015/%";""")
    nnn15=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                nnn15 += urlrow
    print("nnn15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'negynegynegyArticle_tb' where start_url like "%/2016/%";""")
    nnn16=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                nnn16 += urlrow
    print("nnn16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'negynegynegyArticle_tb' where start_url like "%/2017/%";""")
    nnn17=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                nnn17 += urlrow
    print("nnn17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'negynegynegyArticle_tb' where start_url like "%/2018/%";""")
    nnn18=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                nnn18 += urlrow
    print("nnn18 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'origoParagaph_tb' where start_url like "%/2014%";""")
    origo14=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                origo14 += urlrow
    print("origo14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'origoParagaph_tb' where start_url like "%/2015%";""")
    origo15=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                origo15 += urlrow
    print("origo15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'origoParagaph_tb' where start_url like "%/2016%";""")
    origo16=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                origo16 += urlrow
    print("origo16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'origoParagaph_tb' where start_url like "%/2017%";""")
    origo17=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                origo17 += urlrow
    print("origo17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'origoParagaph_tb' where start_url like "%/2018%";""")
    origo18=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                origo18 += urlrow
    print("origo18 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'vsArticle_tb' where time like "%2014%";""")
    vs14=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                vs14 += urlrow
    print("vs14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'vsArticle_tb' where time like "%2015%";""")
    vs15=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                vs15 += urlrow
    print("vs15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'vsArticle_tb' where time like "%2016%";""")
    vs16=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                vs16 += urlrow
    print("vs16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'vsArticle_tb' where time like "%2017%";""")
    vs17=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                vs17 += urlrow
    print("vs17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'vsArticle_tb' where time like "%2018%";""")
    vs18=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                vs18 += urlrow
    print("vs18 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'psArticle_tb' where time like "%2014%";""")
    ps14=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                ps14 += urlrow
    print("ps14 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'psArticle_tb' where time like "%2015%";""")
    ps15=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                ps15 += urlrow
    print("ps15 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'psArticle_tb' where time like "%2016%";""")
    ps16=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                ps16 += urlrow
    print("ps16 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'psArticle_tb' where time like "%2017%";""")
    ps17=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                ps17 += urlrow
    print("ps17 done")
    curr.execute("""SELECT DISTINCT paragaph FROM 'psArticle_tb' where time like "%2018%";""")
    ps18=""
    for row in curr.fetchall():
        urlrow = str(row)
        if urlrow == "":
            continue
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n',"")
        urlrow = urlrow.replace('\\r',"")
        urlrow = urlrow.replace('\\',"")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t',"")     
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urlrow = urlrow.replace('[',"")
        urlrow = urlrow.replace(']',"")
        try:
            detect(urlrow)==hu
        except:
            continue
        else:
            if detect(urlrow)==hu:
                ps18 += urlrow
    print("ps18 done")
    a=[HVG14,HVG15,HVG16,HVG17,HVG18,huszonnegy14,huszonnegy15,huszonnegy16,huszonnegy17,huszonnegy18,index14,index15,index16,index17,index18,nnn14,nnn15,nnn16,nnn17,nnn18,origo14,origo15,origo16,origo17,origo18,vs14,vs15,vs16,vs17,vs18,ps14,ps15,ps16,ps17,ps18]

    for j, _k in enumerate(a):
        words=[]
        w=word_tokenize(_k.lower())
        for word in w:
            words.append(stemmer.stem(word))
        tags=[str(j)]
        tagged_data += [TaggedDocument(words,tags)]
    print(tagged_data)
    
    max_epochs = 2
    vec_size = 300
    alpha = 0.025
     
    model = Doc2Vec(size=vec_size,
                alpha=alpha, 
                min_alpha=0.00025,
                min_count=1,
                dm =1)
    model.build_vocab(tagged_data)
     
    for epoch in range(max_epochs):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)
        model.alpha -= 0.0002
        model.min_alpha = model.alpha
     
    model.save("ady1.model")
    print("Model Saved")
     
         
    model= Doc2Vec.load("ady1.model")
    #to find the vector of a document which is not in training data
    print(model.wv.most_similar("migráns"))
    print(model.docvecs.most_similar([1]))
nlp()
