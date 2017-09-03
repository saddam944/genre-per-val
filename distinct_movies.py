
# coding: utf-8

# In[23]:

import glob, os
import sys
import re
import pandas as pd
import csv
from os.path import basename

path="E:/allusers"
movies=[]
subdirectories = os.listdir(path)
for i in subdirectories:
    with open(path+"/"+i+"/"+i+"_full.csv",'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for mv in rows:
            mvi=mv['movie_title'].replace('"', '').strip()
            movies.append(mvi)

list_unique=(set(movies))

print len(list_unique)


# In[ ]:



