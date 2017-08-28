import re
import gensim
import collections
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import glob, os

filenames=[]
#Keep the all files of directory
path1="C://Users//name//Desktop//IMDB//ur9021307//txt//"
for f1 in os.listdir(path1):
    if f1.endswith(".txt"):
        #print f   
        print "*************"+f1+"********************"
        with open(path1+"//"+f1) as f:
            a=''
            for line in f:
                a=a+line
            tokenizer = RegexpTokenizer(r'\w+')
            raw = a.lower()
            tokens = tokenizer.tokenize(raw)
            en_stop = get_stop_words('en')
            stopped_tokens = [i for i in tokens if not i in en_stop]
            #print stopped_tokens
            #----------------------
            p_stemmer = PorterStemmer()
            texts = [p_stemmer.stem(i) for i in stopped_tokens]
            print texts
            dictionary = corpora.Dictionary([texts])
            corpus = [dictionary.doc2bow(text) for text in [texts]]
            ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
            print(ldamodel.print_topics(num_topics=10))