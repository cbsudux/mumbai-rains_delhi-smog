import plotly.graph_objs as go
import pandas as pd

# Get data
    
def mumbai_bubble_map():
    df = pd.read_csv('mumbai_bubble_map.csv')

    df['text'] = df['city'] + '<br>' + (df['freq']).astype(str)
    limits = [(0,2),(3,10),(11,50),(50,500)]
    colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)"]
    cities = []
    scale = 5 ## 

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[(df['freq'] >=lim[0]) & (df['freq'] <= lim[1])]
        city = dict(
            type = 'scattergeo',
            locationmode = 'India-states',###
            lon = df_sub['lon'],
            lat = df_sub['lat'],
            text = df_sub['text'],
            marker = dict(
                size = df_sub['freq']*scale,
                color = colors[i],
                line = dict(width=0.5, color='rgb(40,40,40)'),
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1]) )
        cities.append(city)

    layout = dict(
            title = 'Hover to learn more. ',
            showlegend = True,

              # margin={'l': 50, 'b': 30, 't': 10, 'r': 0},
            # height=450,
            geo = dict(
                scope='asia',
                projection=dict( type='mercator' ),
                showland = True,
                landcolor = 'rgb(217,217,217)',
                # showocean    = True,
                # oceancolor = 'rgb(0, 0, 0)',

                subunitwidth=1,
                countrywidth=1,
                subunitcolor="rgb(0, 0, 0)",
                countrycolor="rgb(255, 255, 255)",plot_bgcolor="#020202",    paper_bgcolor="#020202"
            ),
        )

    data = cities

    fig = {'data':data,'layout':layout}

    return fig


# Get data
    
def delhi_bubble_map():
    df = pd.read_csv('delhi_bubble_map_data.csv')

    df['text'] = df['city'] + '<br>' + (df['freq']).astype(str)
    limits = [(0,2),(3,10),(11,50),(50,500)]
    colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)"]
    cities = []
    scale = 5 ## 

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[(df['freq'] >=lim[0]) & (df['freq'] <= lim[1])]
        city = dict(
            type = 'scattergeo',
            locationmode = 'India-states',###
            lon = df_sub['lon'],
            lat = df_sub['lat'],
            text = df_sub['text'],
            marker = dict(
                size = df_sub['freq']*scale,
                color = colors[i],
                line = dict(width=0.5, color='rgb(40,40,40)'),
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1]) )
        cities.append(city)

    layout = dict(
            title = 'Click legend to toggle traces.',
            showlegend = True,
            geo = dict(
                scope='asia',
                projection=dict( type='mercator' ),
                showland = True,
                landcolor = 'rgb(217, 217, 217)',
                subunitwidth=1,
                countrywidth=1,
                subunitcolor="rgb(255, 255, 255)",
                countrycolor="rgb(255, 255, 255)"
            ),
        )

    data = cities

    fig = {'data':data,'layout':layout}

    return fig