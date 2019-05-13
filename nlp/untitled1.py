# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:54:58 2019

@author: Athan
"""
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
test_data = word_tokenize("I love chatbots".lower())
v1 = model.infer_vector(test_data)
print("V1_infer", v1)
    