from bs4 import BeautifulSoup
import urllib2
import csv
import pandas as pd
import os



#**************************************main*************************************
username=input("username: ")
#************read**********
with open("%s.csv" %(username), 'r') as f:
    reader = csv.reader(f)
    my_list = list(reader)
    del my_list[0] #delete heading

count=0
newlist=[]
for row in my_list:
    count+=1
    print count
    movie_link=row[6]
    try:
        #**********fetch movie story and genre
        print "\nfetching"
        response2 = urllib2.urlopen(movie_link)
        html_movie=response2.read()
        print "fetched\n"
        
        ind=html_movie.find("inline canwrap")
        ind+=39
        html_movie=html_movie[ind:]

        soup_movie = BeautifulSoup(html_movie)
        storyline=soup_movie.p.get_text() #movie storyline
        storyline=storyline.encode('ascii','ignore') # string

        #*************getting genres*************
        ind=html_movie.find("Genres")
        ind-=86
        html_movie=html_movie[ind:]
        soup_movie = BeautifulSoup(html_movie)
        #print soup_movie.div
        l = soup_movie.div.find_all('a')
        x= l[0].get_text()
        x=x.encode('ascii','ignore') # string
        x = x.strip()                
        genres=x
        for i in range(1, len(l)):
            x= l[i].get_text()
            x=x.encode('ascii','ignore') # string
            x = x.strip()
            genres=genres+","+x

        newlist.append([row[0], storyline, genres, row[3], row[4], row[5], row[6]])
        print "row done"
    except:
        print "******exception*******"
        storyline="-"
        genres="-"
        newlist.append([row[0], storyline, genres, row[3], row[4], row[5], row[6]])

    
csvdataframe=pd.DataFrame(newlist,columns=['movie_title', 'storyline', 'genres', 'date', 'review', 'rating', 'movie link'])
# Create a csv file with the Sentiment Polarity..
csvdataframe.to_csv("IMDB/%s/%s_full.csv"%(username, username),index=False)
print username+" done!"

