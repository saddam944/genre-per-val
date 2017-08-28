import glob, os
import sys
import re
import pandas as pd
import csv

per_val="E:/genre_personality_value_map.csv"
genre=['Action', 'Adventure','Drama','Biography']
score=[]

with open(per_val,'r') as f:
    reader = csv.DictReader(f, delimiter=',')
    rows = list(reader)
    for row in rows:
        if row['GenreA'] in genre:
            score.append([row['user_id'],row['Open'], row['Concen'], row['Extra'], row['Agree'], row['Neuro'], row['Conservation'], row['Hedonism'], row['Self-enhan'], row['Self-trans'], row['Openness_to'], row['GenreA'], row['GenreB'], row['Rate']])
        
csvdataframe=pd.DataFrame(score,columns=['user_id', 'Open', 'Concen', 'Extra', 'Agree', 'Neuro', 'Conservation','Hedonism','Self-enhan', 'Self-trans', 'openness-to-change', 'Genre-1', 'Genre-2','Rate'])
csvdataframe.to_csv("E:/selected_genre.csv",index=False)



