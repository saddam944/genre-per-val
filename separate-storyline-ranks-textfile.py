import glob, os
import sys
import re
import pandas as pd
import csv
from os.path import basename
   

#path="C:/Users/saddam/Dropbox/paper work/Euna Work/Dynamic user modelling/IMDB"
path="E:/im"
subdirectories = os.listdir(path)
for i in subdirectories:
    with open(path+"/"+i+"/"+i+"_full.csv",'r') as f:
        cnt=0
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for row in rows:
            if row['storyline']!=" ":
                cnt+=1
            #print row['storyline']
                with open("D:/"+str(cnt)+"_"+i+"_"+row['rating']+".txt", "w") as f:
                    f.write(row['storyline'])




