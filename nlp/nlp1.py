# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:02:01 2019

@author: Athan
"""
import sqlite3
import nltk
from nltk.tokenize import word_tokenize
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

def get_tokens(text):
    tokens = word_tokenize(text)
    return [token.lower() for token in tokens]
print()
    
def hvgclean():
#    assert gensim.models.doc2vec.FAST_VERSION > -1
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT paragaph FROM 'hvgArticle_tb';
                 """)
    articlesHVG=""
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
        urlrow = urlrow.replace('"',"")
        articlesHVG = articlesHVG + urlrow
    print(articlesHVG)
    return articlesHVG

def huszonnegyclean():
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT paragaph FROM 'huszonnegyhuArticle_tb';
                 """)
    articleshuszonnegy=""
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
        urlrow = urlrow.replace('Kiemelt kép:',"")
        urlrow = urlrow.replace('"',"")
        urlrow = urlrow.replace('/'," ")
        articleshuszonnegy += urlrow
    print(articleshuszonnegy)
    return articleshuszonnegy

def indexclean():
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT paragaph FROM 'indexArticle_tb';
                 """)
    articlesindex=""
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
        urlrow = urlrow.replace('Köszönjük hogy olvasol minket! Ha fontos számodra a független sajtó fennmaradása támogasd az Indexet!',"")
        urlrow = urlrow.replace('Köszönjük hogy minket olvasol minden nap! Ha szeretnél még sokáig sok ilyen vagy még jobb cikket olvasni az Indexen ha szeretnéd ha még lenne független nagy elérésű sajtó Magyarországon amit vidéken és a határon túl is olvasnak akkor támogasd az Indexet!                                                       Tudj meg többet az Index támogatói kampányáról!                                               Milyen rendszerességgel szeretnél támogatni minket? Mekkora összeget tudsz erre szánni? Mekkora összeget tudsz erre szánni?',"")
        urlrow = urlrow.replace(',',"")
        articlesindex += urlrow
    print(articlesindex)
    return articlesindex

def negynegynegyclean():
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT paragaph FROM 'negynegynegyArticle_tb';
                 """)
    articles444=""
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
        urlrow = urlrow.replace('"',"")
        urlrow = urlrow.replace('A 444-et itt Direkt36-ot pedig itt ',"")
        articles444 += urlrow
    print(articles444)
    return articles444
def origoclean():
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT paragaph FROM 'origoArticle_tb';
                 """)
    articlesorigo=""
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
        urlrow = urlrow.replace('"',"")
        urlrow = urlrow.replace('/'," ")
        articlesorigo += urlrow
    print(articlesorigo)
    return articlesorigo

def  vsclean():
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    curr.execute("""SELECT paragaph FROM 'vsArticle_tb';
                 """)
    articlesvs=""
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('\\xa0',' ')
        urlrow = urlrow.replace('\xa0',' ')
        urlrow = urlrow.replace('\\n'," ")
        urlrow = urlrow.replace('\\r'," ")
        urlrow = urlrow.replace('\\'," ")
        urlrow = urlrow.replace('\\xadt'," ")
        urlrow = urlrow.replace('\\t'," ")     
        urlrow = urlrow.replace('('," ")
        urlrow = urlrow.replace(')'," ")
        urlrow = urlrow.replace("'"," ")
        urlrow = urlrow.replace("-"," ")
        urlrow = urlrow.replace(','," ")
        urlrow = urlrow.replace('"'," ")
        urlrow = urlrow.replace('/'," ")
        urlrow = urlrow.replace(' t '," ")
        urlrow = urlrow.replace(' tt '," ")
        urlrow = urlrow.replace('ttt'," ")
        urlrow = urlrow.replace('tttt'," ")
        urlrow = urlrow.replace('ttttt'," ")
        urlrow = urlrow.replace('tttttt'," ")
        urlrow = urlrow.replace('ttttttt'," ")
        urlrow = urlrow.replace('tttttttt'," ")
        urlrow = urlrow.replace(' t '," ")
        urlrow = urlrow.replace(" tt"," ")
        urlrow = urlrow.replace(' t '," ")
        urlrow = urlrow.replace(' t '," ")
        articlesvs += urlrow
    print(articlesvs)
    return articlesvs

vsclean()
tagged_data = word_tokenize(articlesHVG.lower())
    model = Word2Vec(min_count=20,
                     window=2,
                     size=300,
                     sample=6e-5, 
                     alpha=0.03, 
                     min_alpha=0.0007, 
                     negative=20,
                     workers=3)
    model.build_vocab([tagged_data])

    for epoch in range(10):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)
        model.alpha -= 0.0002
        model.min_alpha = model.alpha

    model.save("hvgw2v.model")
    print("Model Saved")
    len(model)

    
    
#nlp()
    
    
    
    
    
    
    
    
    
#    sentence = []
#    sentence = [get_tokens(doc) for doc in a]
#    model_ng = gensim.models.word2vec.Word2Vec(sentence,min_count=3, size=200)
#    model_ng.most_similar("bevándorló")
#    for i in enumerate(sentence):
#        tagged_documents.append(TaggedDocument(sent,["sent_{}".format(i)])
#    d2v_model = gensim.models.doc2vec.Doc2Vec(tagged_documents, size=300)
#    d2v_model.most_similar("menekült")
#    from gensim.models.doc2vec import TaggedDocument
#    
#
#    
        
