import plotly
import pandas as pd
from pymongo import MongoClient
import geonamescache


client = MongoClient()
db = client.delhi_tweets_loc
collection = db.twitter_collection


gc = geonamescache.GeonamesCache()


df_loc = pd.DataFrame()
df_loc['city'] = []
df_loc['lat'] = []
df_loc['lon'] = []


tweets_iterator = collection.find()
city = []
lat = []
lon = []

for tweet in tweets_iterator:
    city_name =  tweet['place']['name']
    list_temp = gc.get_cities_by_name(city_name)
    if len(list_temp)!= 0:
        for x in list_temp[0].values():
            city.append(city_name)
            lat.append(x['latitude'])
            lon.append(x['longitude'])
df_loc['city'] = city
df_loc['lat'] = lat
df_loc['lon'] = lon

df_loc['freq'] = df_loc.groupby('city')['city'].transform('count')
df_loc = df_loc.drop_duplicates()
df_temp = df_loc.copy()
df_temp.columns = ['city','start_lat','start_lon','cnt']

end_lat = 28.63576
end_lon = 77.22445
df_temp['end_lat'] = [end_lat for i in range(0,len(df_temp)) ]
df_temp['end_lon'] = [end_lon for i in range(0,len(df_temp)) ]
df_links = df_temp
df  = df_loc
df_links = df_links.reset_index(drop=True)


# Plotting

cities = [ dict(
        type = 'scattergeo',
        lon = df['lon'],
        lat = df['lat'],
        hoverinfo = 'text',
        text = df['city'],
        mode = 'markers',
        marker = dict( 
            size=2, 
            color='rgb(255, 0, 0)',
            line = dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        ))]
        
links = []
for i in range( len( df_temp )):
    links.append(
        dict(
            type = 'scattergeo',
           
            lon = [ df_links['start_lon'][i], df_links['end_lon'][i] ],
            lat = [ df_links['start_lat'][i], df_links['end_lat'][i] ],
            
            mode = 'lines',
            line = dict(
                width = 1,
                color = 'red',
            ),
#             opacity = float(df_links['cnt'][i])/float(df_links['cnt'].max()),
        )
    )
    
layout = dict(
        title = 'Non-Delhi twitter Activity<br>(Hover for city names)',
        showlegend = False, 
        geo = dict(
            scope='asia',
            projection=dict( type='mercator' ),
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
            
        ),
    )
    
fig = dict( data=links + cities, layout=layout )
plotly.offline.plot( fig, filename='negative location' )

