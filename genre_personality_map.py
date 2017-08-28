import glob, os
import sys
import re
import pandas as pd
import csv
import numbers


# In[82]:

def imdb_personality_map():    
    imdb="E:/user_model/files/topic_modeling.csv"
    per_val="E:/user_model/files/psychological_scores.csv"
    per_score=[]
    for line in open(imdb):
        try:
            splitter=line.split("]\", ,")
            user=splitter[0].split(',')
            first_genre=splitter[1].split(',')
 
            if user[0]!=" " and first_genre!=" ":
                for rating in first_genre:
                    if rating.isdigit():
                        with open(per_val,'r') as f:
                            reader = csv.DictReader(f, delimiter=',')
                            rows = list(reader)
                            for row in rows:
                                if row['ids']==user[0]:
                                    per_score.append([user[0], row['Open'], row['Concen'], row['Extra'], row['Agree'], row['Neuro'], row['Conservation'], row['Hedonism'], row['Self-enhan'], row['Self-trans'], row['Openness_to'], first_genre[0], first_genre[1], rating])
                                                       
        except:
            continue

    csvdataframe=pd.DataFrame(per_score,columns=['user_id', 'Open', 'Concen', 'Extra', 'Agree', 'Neuro', 'Conservation','Hedonism','Self-enhan', 'Self-trans', 'openness-to-change', 'Genre-1', 'Genre-2','Rate'])
    csvdataframe.to_csv("E:/user_model/files/genre_personality_value_map.csv",index=False)

if __name__ == '__main__':
        imdb_personality_map()
        #personality_value()
