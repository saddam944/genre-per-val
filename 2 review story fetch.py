from bs4 import BeautifulSoup
import urllib2
import csv
import pandas as pd
import os

def create_folder(user_link):
    username=user_link[25:-1]
    newpath = "IMDB\\%s" %(username)
    newpath2 = "IMDB\\%s\\txt" %(username)
    
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    if not os.path.exists(newpath2):
        os.makedirs(newpath2)    
                
    return username


#**************************************main*************************************
#************read**********
with open("2 input.csv", 'r') as f:
    reader = csv.reader(f)
    my_list = list(reader)
    del my_list[0] #delete heading


#**************for one user*************
row=my_list[0]
user_link=row[0]
username = create_folder(user_link) #create_folder for this user
csv_content_list=[]
    
user_link=user_link+"comments?order=date&start="    


pageno=0
while 1: #iterates for one user's pages of reviews
    #***************for one page of pagination***********
    user_link=user_link+str(pageno)
    pageno+=10

    #now fetch data from user_link
    try:
        response = urllib2.urlopen(user_link)
        html = response.read() #html is string

        while 1: #iterates over reviews in one page
            try:
                ind=html.find("background: #eeeeee; clear:both")
                if(ind==-1):
                    break
                ind-=16
                html=html[ind:]

                soup = BeautifulSoup(html)#starts from a p tag
                movie_title = soup.p.div.a.get_text() #movie name/title
                movie_title=movie_title.encode('ascii','ignore') # string

                title_link = soup.p.div.a['href']  #movie title href link
                title_link = title_link.encode('ascii','ignore') # string

                l=soup.find_all('p')
                review=l[1].get_text() #review
                review=review.encode('ascii','ignore') # string
                if review.find("This review may contain spoilers")!=-1:
                    review=l[2].get_text() #review
                    review=review.encode('ascii','ignore') # string

                rating=soup.p.b.get_text()#rating i.e 8/10
                rating= rating.encode('ascii','ignore') # string
                ind=rating.find("/")
                rating=rating[:ind] #rating i.e 8
                #print rating #rating i.e 8

                date = soup.p.small.get_text() #date
                date=date.encode('ascii','ignore') # string
                if date.find("found the following review useful")!=-1:
                    l2=soup.find_all('small')
                    date=l2[1].get_text() #date
                    date=date.encode('ascii','ignore') # string
                    

                #**********fetch movie story and genre
                movie_link="http://www.imdb.com"+title_link
                response2 = urllib2.urlopen(movie_link)
                html_movie=response2.read()
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

                #got review and movie info for one movie
                '''print storyline
                print date
                print "\n"'''
                #print review
                print movie_title
                csv_content_list.append([movie_title.strip(), storyline.strip(), genres, date.strip(), review.strip(), rating])

                #write this review in a text file named after the movie title
                #now write in txt file
                if movie_title.find(":"):
                    textfile = movie_title.replace(":", "-")
                wrfile=open("IMDB/"+username+"/txt/"+textfile+".txt", 'w')
                wrfile.write(review.strip())
                wrfile.close()

                #go to next review
                ind=html.find("background: #eeeeee; clear:both")
                html=html[ind+6:]
                    

            except:
                print "************exception in inner while***********"
                #go to next review
                ind=html.find("background: #eeeeee; clear:both")
                html=html[ind+6:]
                continue
            
    except:
        print "************exception in outer while***********"
        print pageno
        print movie_title
        break #end of reviews
        
#collected all reviews for one user
csvdataframe=pd.DataFrame(csv_content_list,columns=['movie_title', 'storyline', 'genres', 'date', 'review', 'rating'])
# Create a csv file with the Sentiment Polarity..
csvdataframe.to_csv("IMDB/%s/%s.csv"%(username, username),index=False)
print username+" done!"


    

