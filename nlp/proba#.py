from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from langdetect import detect
from nltk.stem.snowball import SnowballStemmer


lang = detect("kurvara nem tudom hogy mi a fasz baja van")
b="""Góg és Magóg fia vagyok én
Hiába döngetek kaput falat
S mégis megkérdem tőletek
Szabad-e sírni a Kárpátok alatt

Verecke híres útján jöttem én
Fülembe még ősmagyar dal rivall
Szabad-e Dévénynél betörnöm
Új időknek új dalaival

Fülembe forró ólmot öntsetek
Legyek az új az énekes Vazul
Ne halljam az élet új dalait
Tiporjatok reám durván gazul

De addig sírva, kínban, mit se várva
Mégiscsak száll új szárnyakon a dal
S ha elátkozza százszor Pusztaszer
Mégis győztes mégis új és magyar"""

c="""Útra kelünk Megyünk az Őszbe
Vijjogva sírva kergetőzve
Két lankadt szárnyú héja-madár
Új rablói vannak a Nyárnak
Csattognak az új héja-szárnyak
Dúlnak a csókos ütközetek

Szállunk a Nyárból űzve szállunk
Valahol az Őszben megállunk
Fölborzolt tollal szerelmesen

Ez az utolsó nászunk nékünk
Egymás husába beletépünk
S lehullunk az őszi avaron"""

a = [b,c]

stemmer = SnowballStemmer("hungarian")

tag_data = []
for j, _k in enumerate(a):
    words=[]
    w=word_tokenize(_k.lower())
    for word in w:
        words.append(stemmer.stem(word))
    tags=[str(j)]
    tag_data += [TaggedDocument(words,tags)]

max_epochs = 10
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=vec_size,
            alpha=alpha, 
            min_alpha=0.00025,
            min_count=1,
            dm =1)
model.build_vocab(tag_data)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tag_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    model.alpha -= 0.0002
    model.min_alpha = model.alpha

model.save("p2v.model")
print("Model Saved")

    
model= Doc2Vec.load("p2v.model")
#to find the vector of a document which is not in training data
docvec = model.docvecs[1]
print(model.wv.most_similar("van"))
