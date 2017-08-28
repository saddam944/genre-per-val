from imdb import IMDb
import urllib2
import csv
import pandas as pd
import os


username=input("username: ")
#************read**********
with open("%s_full.csv" %(username), 'r') as f:
    reader = csv.reader(f)
    my_list = list(reader)
    del my_list[0] #delete heading

count=0
newlist=[]
ia = IMDb()
for row in my_list:
    
    count+=1
    #print count
    
    if row[1]!="-":#already ase
        newlist.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
        continue
    
    
    movie_link=row[6]
    movieid=movie_link[28:35]

    try:
        #**********fetch movie story and genre
        print "\nfetching"
        movie = ia.get_movie(movieid)
        print "fetched\n"

        genreList=movie['genres']#list of unicodes
        plotList= movie['plot']#list of unicodes

        genres=""
        g=genreList[0] # g is a unicode
        g=g.encode('ascii','ignore') # now g is a string
        genres=g
        for i in range(1, len(genreList)):
            g=genreList[i] # g is a unicode            
            g=g.encode('ascii','ignore') # now g is a string
            
            genres=genres+","+g


        plots=""
        plot=plotList[0] # plot is a unicode
        plot=plot.encode('ascii','ignore') # now plot is a string
        plots=plot
        for i in range(1, len(plotList)):
            plot=plotList[i] # plot is a unicode            
            plot=plot.encode('ascii','ignore') # now plot is a string
            
            plots=plots+".:::."+plot
        
        #plots delimeter .:::.
        #genres delimeter ,
        newlist.append([row[0], plots, genres, row[3], row[4], row[5], row[6]])
        print "row done"
    except:
        print "******exception*******"
        plots="-"
        genres="-"
        newlist.append([row[0], plots, genres, row[3], row[4], row[5], row[6]])

    
csvdataframe=pd.DataFrame(newlist,columns=['movie_title', 'storyline', 'genres', 'date', 'review', 'rating', 'movie link'])
# Create a csv file with the Sentiment Polarity..
csvdataframe.to_csv("%s_full.csv"%(username),index=False)


print username+" done!"

