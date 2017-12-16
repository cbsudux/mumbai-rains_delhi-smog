from pymongo import MongoClient
import tweepy
from tweepy import AppAuthHandler
import seaborn as sns
import json
import pandas as pd

%matplotlib inline

# Dbase for tweets with location
client = MongoClient()
db = client.delhi_tweets_loc
collection = db.twitter_collection


text = []
hashtags = []

tweets_iterator = collection.find()
for tweet in tweets_iterator:
    text.append(tweet['text'])
    for i in tweet['entities']['hashtags']:     
        hashtags.append(i['text'])


df_hashtags = pd.DataFrame()
df_hashtags['hashtags'] = hashtags

df_hashtags.head()

df_hashtags = df_hashtags.apply(lambda x: x.astype(str).str.lower())

df_freq = df_hashtags['hashtags'].value_counts()

df_hashtags['freq'] = df_hashtags.groupby('hashtags')['hashtags'].transform('count')


df_hashtags.groupby(['hashtags'], as_index = False)[['freq']].sum()
