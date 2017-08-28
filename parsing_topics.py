import csv
import pandas as pd
import re
import time
from collections import Counter
import string


def separate_topic_frequency():
    score=[]
    ttopic=[]
    user=[]
    path="C:/Users/user/Desktop/rated_topics_.csv"
    with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        cntr=0
        for row in rows:
            tpc=row['Topics'].split('*')
            for wrd in tpc:
                w=wrd.split('+')
                for w1 in w:
                    if cntr%2==1:
                        user.append([row['User_id']])
                        s = re.sub(r'^"|"$', '', w1)
                        s1=str(s).replace('\"','')
                        ttopic.append([s1])
                    if cntr%2==0:
                        score.append([w1])                    
                    cntr+=1
    csvdataframe=pd.DataFrame(data=dict(Userid=user,topics=ttopic,probability=score))
    csvdataframe.to_csv("E:/tyt.csv",index=False)
    time.sleep(2)

def parse_again():
    path="E:/tyt.csv"
    usr=[]
    scr=[]
    tpc=[]
    with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for row in rows:
            usr.append([str(row['Userid'])[2:-2]])
            scr.append([str(row['probability'])[2:-2]])
            tpc.append([str(row['topics'])[2:-2]])
    csvdataframe=pd.DataFrame(data=dict(Userid=usr,topics=tpc,probability=scr))
    csvdataframe.to_csv("E:/t.csv",index=False)

def remove_s():
    path="E:/t.csv"
    usr=[]
    scr=[]
    tpc=[]
    with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for row in rows:
            m=row['topics'].strip()
            if m!= "s":
                usr.append([row['Userid']])
                tpc.append([row['topics']])
                scr.append([row['probability']])
        csvdataframe=pd.DataFrame(data=dict(Userid=usr,topics=tpc,probability=scr))
        csvdataframe.to_csv("E:/withoutS.csv",index=False)
        
def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

def remove_duplicate():
    path="E:/withoutS.csv"
    usr=[]
    scr=[]
    tpc=[]
    with open(path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = list(reader)
        for row in rows:
            tpc.append([row['topics']])
    a=sort_and_deduplicate(tpc)
    for w in a:
        print str(w)[4:-4]
    


    

if  __name__ =='__main__':
    #separate_topic_frequency()
    #time.sleep(3)
    #parse_again() # No need this module actually
    #remove_s()
    #remove_duplicate()

