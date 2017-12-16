# TO do : Adjust scale 
# Make bg black

from pymongo import MongoClient
import pandas as pd
import plotly.graph_objs as go
import plotly


client = MongoClient()
db = client.mumbai_tweets_noloc_edited
collection = db.twitter_collection


time = []
tweets_iterator = collection.find()
for tweet in tweets_iterator:
        time.append(tweet['created_at'])

import datetime

datetime.datetime.strptime('Sun Dec 10 10:29:24 +0000 2017','%a %b %d %H:%M:%S +%f %Y').strftime('%H:00:00 %Y-%m-%d')

time_conv = []
for i in time:
    time_conv.append(datetime.datetime.strptime(i,'%a %b %d %H:%M:%S +%f %Y').strftime('%Y-%m-%d %H:00:00'))

len(time_conv)

df_time = pd.DataFrame()
df_time['date'] = time_conv 


df = df_time

df['freq'] = df.groupby('date')['date'].transform('count')


df = df.drop_duplicates()

df = df.reset_index(drop=True)

reversed_df = df.iloc[::-1]

df = reversed_df

df = df.reset_index(drop=True)

df



trace_high = go.Scatter(
    x=df.date,
    y=df['freq'],
    name = "freq",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

data = [trace_high]

layout = dict(
    title='Tweet Activity VS Time<b>(Play with the rangeslider for precision)',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='all',
                     step='day',
                     stepmode='backward'),
                dict(count=6,
                     label='1d',
                     step='hour',
                     stepmode='backward'),
            ])
        ),
        rangeslider=dict(autorange = True),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename = "Tweet Activity Vs Time ")




