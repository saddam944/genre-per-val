import re
import gensim
import collections
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import glob, os
import csv
import pandas as pd

filenames=[]
#Keep the all files of directory
path1="D:/Low rating/"
for f1 in os.listdir(path1):
    if f1.endswith(".txt"):
        #print f   
        print "*************"+f1+"********************"
        users=[]
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
            #print texts
            dictionary = corpora.Dictionary([texts])
            corpus = [dictionary.doc2bow(text) for text in [texts]]
            ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
            topic=ldamodel.print_topics(num_topics=10)
            uid=f1.split('_')
            #print topic
            #print uid[0]
            #print uid[1]
            users.append([uid[0],topic,uid[1]])
            csvdataframe=pd.DataFrame(users,columns=['User_id', 'Topics', 'Ranks'])
            csvdataframe.to_csv("D:/Low Rating Topics/"+uid[0]+"_.csv",index=False)

