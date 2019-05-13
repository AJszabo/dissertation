# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:26:01 2019
@author: Domos
"""
import pandas as pd
from sklearn.manifold import TSNE
import re
import matplotlib.pyplot as plt

from nltk.stem.snowball import SnowballStemmer
from sklearn.decomposition import PCA  
from gensim.models.doc2vec import Doc2Vec
from matplotlib import pyplot
from scipy import spatial
model= Doc2Vec.load("migrationfinal.model")
#to find the vector of a document which is not in training data

#stemmer = SnowballStemmer("hungarian")
#print(stemmer.stem("nagylak"))
#print(model.wv.most_similar(positive="migráns"))
#print(model.wv.most_similar(positive="fidesz"))
#print(model.wv.most_similar(positive="isis"))
#print(model.wv.most_similar(positive="rösz"))
#print(model.wv.most_similar(positive="london"))
#print(model.wv.most_similar(positive="eu"))
#result = model.wv.most_similar(positive=['párizs', 'franciaország'], negative=['brüsszel'], topn=1)
#print(result)
#result = model.wv.most_similar(positive=['férfi', 'apa'], negative=['nő'], topn=1)
#print(result)
#result = model.wv.most_similar(positive=['gyurcsány', 'dk'], negative=['orbán'], topn=3)
#print(result)
#print("""order:
#    hvg  24  index 444  origo   vs    ps
#    0-4 5-9 10-14 15-19 20-24 25-29 30-34
#      """)
print(model.docvecs.most_similar(positive=['11'] ,topn=5))
print(model.docvecs.most_similar(positive=['21'] ,topn=5))
print(model.docvecs.most_similar(positive=['34'] ,topn=5))
print(model.docvecs.most_similar(positive=['18'] ,topn=5))


#X = model[vocab]
#tsne = TSNE(n_components=2)
#X_tsne = tsne.fit_transform(X[:1000,:])
#df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#
#ax.scatter(df['x'], df['y'])
#
#for word, pos in df.iterrows():
#    ax.annotate(word, pos)

#for j in range(7):     
#    a = (j * 5)+4
#    similar_doc = model.docvecs.most_similar(str(a),topn=34)
#    print(a)
#    for i in range(7):
#        b = (i * 5)+4
#        print([item for item in similar_doc if item[0] == str(b) ])
    

#print("""order:
#    hvg  24  index 444  origo   vs    ps
#    0-4 5-9 10-14 15-19 20-24 25-29 30-34
#      """)
#a=[0,1,2,3,4,5,6]
#b =[]
#c =[]
#d=0
#l=0
#m=0
#for i in a :
#    for j in a:

#        l=j*5
#        m=i*5 
#        b.append(model.docvecs.n_similarity(str(l),str(m)))
#        d+=model.docvecs.n_similarity(str(l),str(m))
##        print(l)
##        print(m)
#    c.append(b)
#    print(b)
#    b=[]
#print((d-7)/42)
#
#print(model.docvecs.n_similarity('3', '33'))

#X = model[model.wv.vocab.get("migráns")]
#pca = PCA(n_components=2)
#result = pca.fit_transform(X)
## create a scatter plot of the projection
#pyplot.scatter(result[:, 0], result[:, 1])
#words = list(model.wv.vocab.get("migráns"))
#for i, word in enumerate(words):
#	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
#pyplot.show()

#model.wv.similarity(w1,w2)