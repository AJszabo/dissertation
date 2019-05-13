# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:42:42 2019

@author: Domos
"""
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
    a=[ps14,ps15,ps16,ps17,ps18]

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
     
    model.save("ps.model")
    print("Model Saved")
     
         
    model= Doc2Vec.load("ps.model")
    #to find the vector of a document which is not in training data
    print(model.wv.most_similar("migráns"))
    print(model.docvecs.most_similar([1]))
nlp()
