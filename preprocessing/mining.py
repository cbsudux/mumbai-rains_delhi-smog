from pymongo import MongoClient
import tweepy
from tweepy import AppAuthHandler
import seaborn as sns
import json
import pandas as pd

%matplotlib inline

# Search API App 1

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = AppAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if not api:
    print("Can't authenticate")

# Dbase for tweets with location
client = MongoClient()
db = client.delhi_tweets_loc
collection = db.twitter_collection


# Lang = en
# More query terms
# India id id='b850c1bfd38f30e0'
# earliest post --> db.twitter_collection.find().sort({'id':1}).limit(1)

search_query = '#delhismog OR #smogindelhi'
count_tweet = 0
count_loc = 0
for tweet in tweepy.Cursor(api.search, q=search_query, rpp =100,lang = 'en').items():
        
    count_tweet = count_tweet +1
    
    print(count_tweet,' ',count_loc)

    collection.insert_one(tweet._json)
