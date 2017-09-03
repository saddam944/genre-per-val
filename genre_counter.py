
# coding: utf-8

# In[17]:

import glob, os
import sys
import re
import pandas as pd
import csv
import numbers
from collections import Counter

path="E:/FinalGenre.csv"
gen=[]
with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for i in rows:
            gen.append(i['genre'])
Counter(gen)



#print list_unique


# In[ ]:



