import glob, os
import sys
import re
import pandas as pd
import csv
import gensim
import collections
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from os.path import basename


def imdb_twitter_id():
    fields = ['Author name','year','movie name','imdb_profile', 'twitter_profile']

    df = pd.read_csv('E:/imdb/imdb-twitter-username.csv', skipinitialspace=True, usecols=fields)

    #Slicing substring from the links
    profile=df.imdb_profile.str[25:len(df.imdb_profile)]
    twpro=df.twitter_profile.str[20:len(df.twitter_profile)]
    csvdataframe=pd.DataFrame(data=dict(Imdb_Profile=profile, Twitter_profile=twpro)) #writing two series to a dataframe together
    #csvdataframe.to_csv("tts.csv",index=False)
    return csvdataframe
            
def twittername_imdbid_matching(): #Reorganize the userid with the csv file
    #Get twitter name and ids together
    twt_imdb=imdb_twitter_id()
    #print type(twt_imdb)    
    path="E:/imdb/allscores.csv"
    with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
    for row in rows:
        #print row['Filename']
        for index, rw in twt_imdb.iterrows():#iterating dataframe
            if row['Filename']==rw['Twitter_profile']: #Comaparing dataframe string with csv user name
                print rw['Imdb_Profile']  
                
def create_csv(): #Create csv for keeping data after topic modeling
    with open('E:/output.csv', 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['user_id', 'topic','genre','rating'])
        
def lda_compute(user_id, a,genre, rating):
            tokenizer = RegexpTokenizer(r'\w+')
            raw = a.lower()
            tokens = tokenizer.tokenize(raw)
            en_stop = get_stop_words('en')
            stopped_tokens = [i for i in tokens if not i in en_stop]
            #print stopped_tokens
            #----------------------
            p_stemmer = PorterStemmer()
            texts = [p_stemmer.stem(i) for i in stopped_tokens]
            dictionary = corpora.Dictionary([texts])
            corpus = [dictionary.doc2bow(text) for text in [texts]]
            ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
            uid=str(user_id).rsplit('/',1)
            uidf=uid[1].rsplit('_',1)
            uidl=uidf[0]
            #print uidl
            #print(ldamodel.print_topics(num_topics=5))
            #print rating
            #print genre
            write_to_csv(uidl,ldamodel.print_topics(num_topics=5),genre,rating)
                
def story_rating():
    #fields = ['movie_title', 'storyline','genres','date','review','rating','movie link']
    path="E:/imdb/"
    subdirectories = os.listdir(path)
    for f in subdirectories:
        p1=path+f+"/"+f+"_full.csv"
        with open(p1,'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            rows = list(reader)
        for row in rows:
            if row['storyline']: #caution: no storyline should be empty
                lda_compute(f,row['storyline'], row['genres'], row['rating'])
            else:
                continue
            #print row['storyline']
            #print row['rating']    
            
def write_to_csv(id,topic,genre,rating ):
    writer = csv.writer(open("E:/output.csv", "ab"), delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([id,topic,genre,rating])
    return True

                
if __name__ == '__main__':
    #twittername_imdbid_matching()
    #create_csv()
    story_rating()
    



