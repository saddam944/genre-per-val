import tweepy #https://github.com/tweepy/tweepy
import pandas as pd
import csv
access_key = "your access key"
access_secret = "your secret"
consumer_key = "consumer consumer key"
consumer_secret = "consumer secret key"
screen_name="username"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
alltweets = []	
new_tweets = api.user_timeline(screen_name = screen_name,count=200)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1
while len(new_tweets) > 0:
    print("getting tweets before %s" % (oldest))
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    print("...%s tweets downloaded so far" % (len(alltweets)))
    
outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
dataframe=pd.DataFrame(outtweets,columns=['twitter_id','date','tweet'])
dataframe.to_csv("%s_.csv"%(screen_name),index=False)