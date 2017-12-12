import plotly
import pandas as pd


def mumbai_linemap():

    df  = pd.read_csv('mumbai_linemap_cities.csv')
    df_flight_paths = pd.read_csv('mumbai_line_map_data.csv')
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
            
    flight_paths = []
    for i in range( len( df_flight_paths )):
        flight_paths.append(
            dict(
                type = 'scattergeo',
               
                lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
                lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
                
                mode = 'lines',
                line = dict(
                    width = 1,
                    color = 'red',
                ),
    #             opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
            )
        )
        
    layout = dict(
            title = 'Hover to learn more.',
            showlegend = False, 
            geo = dict(
                scope='asia',
                projection=dict( type='mercator' ),
                showland = True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(204, 204, 204)',
                
            ),
        )
        
    fig = dict( data=flight_paths + cities, layout=layout )

    return fig


def delhi_linemap():
    df  = pd.read_csv('delhi_linemap_cities.csv')
    df_flight_paths = pd.read_csv('delhi_linemap_data.csv')

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
            
    flight_paths = []
    for i in range( len( df_flight_paths )):
        flight_paths.append(
            dict(
                type = 'scattergeo',
               
                lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
                lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
                
                mode = 'lines',
                line = dict(
                    width = 1,
                    color = 'red',
                ),
    #             opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
            )
        )
        
    layout = dict(
            # title = 'Non-Delhi twitter Activity<br>(Hover for city names)',
            showlegend = False, 
            geo = dict(
                scope='asia',
                projection=dict( type='mercator' ),
                showland = True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(204, 204, 204)',
                
            ),
        )
        
    fig = dict( data=flight_paths + cities, layout=layout )
    return fig
