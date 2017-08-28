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
        tot_rat=0
        story_line=''
        print i
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        try:
            for row in rows:
                if row['storyline']!=' ' and row['rating']!=' ':
                    rate=float(row['rating'].strip())
                    if rate>7:
                        cnt+=1
                        tot_rat+=rate
                        story_line=story_line+row['storyline']
            #print ("Average Rate*******",round(float(tot_rat/cnt),2))
            avg=round(float(tot_rat/cnt),2)
            with open("D:/"+i+"_"+str(avg)+"_"+".txt", "w") as f:
                f.write(story_line)
        except:
            continue
                    

