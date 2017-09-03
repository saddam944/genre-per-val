
# coding: utf-8

# In[3]:

import glob, os
import sys
import re
import pandas as pd
import csv
import numbers

path="E:/FinalGenre.csv"
gen=[]
with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for i in rows:
            gen.append(i['genre'])

list_unique=(set(gen))

print list_unique


# In[ ]:



