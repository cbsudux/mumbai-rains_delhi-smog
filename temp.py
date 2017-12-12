import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from bubble_map_helpers import *
from line_map_helpers import *
from network_graph_helpers import *
from time_series_helpers import *
import base64
from text_image import *
from retweet_otweet import *

# Build server

app = dash.Dash(__name__)
server = app.server


"""

Row : title
Row : map + map

"""
image_filename = 'wordcloud_mumbai.png' # replace with your own image
encoded_image_1 = base64.b64encode(open(image_filename, 'rb').read())

image_filename = 'wordcloud_delhi.png' # replace with your own image
encoded_image_2 = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div(
                        [
                            # Row :title
                            html.Div(
                                        [                                
                                            html.H1('Twitter tweet analysis',className = 'text-center')
                                        ],className = 'row'
                                    ),

                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                             html.H2('#MumbaiRains',className = 'text-center')
                                        

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                             html.H2('#DelhiSmog',className = 'text-center')
                                                            ],className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),                           

                            #Row : title + title

                            html.Div(),


                            #Row : map + map

                            html.Div(
                                        [                                
                                            html.H4('Twitter activity bubble map',className = 'text-center')
                                        ],className = 'row'
                                    ),

                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'mumbai-bubble-map',
                                                                            figure = mumbai_bubble_map()
                                                                        )

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'delhi-bubble-map',
                                                                            figure = delhi_bubble_map()
                                                                        )

                                                            ],
                                                            className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),                    
                            html.Div(
                                        [                                
                                            html.H4('Non-Delhi/Mumbai tweets',className = 'text-center')
                                        ],className = 'row'
                                    ),

                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'mumbai-line-map',
                                                                            figure = mumbai_linemap()
                                                                        )

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'delhi-line-map',
                                                                            figure = delhi_linemap()
                                                                        )

                                                            ],
                                                            className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),

                            # Row :title
                            html.Div(
                                        [                                
                                            html.H4('Kamada-Kawai user mention\'s graph',className = 'text-center')
                                        ],className = 'row'
                                    ),

                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            
                                                                dcc.Graph(
                                                                            id = 'mumbai-network-graph',
                                                                            figure = mumbai_get_graph()
                                                                        )

                                                            # , style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'middle'}, 

                                                            ,className='six columns'
                                                        ),


                                            ],
                                            
                                    ),


                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            
                                                                dcc.Graph(
                                                                            id = 'delhi-network-graph',
                                                                            figure = delhi_getget_graph()
                                                                        )

                                                            # , style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'middle'}, 

                                                            ,className='six columns'
                                                        ),


                                            ],
                                            className = 'row'
                                    ),
                            html.Div(
                                        [                                
                                            html.H4('Twitter activity vs time ( About a week )',className = 'text-center')
                                        ],className = 'row'
                                    ),

                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'mumbai-time-map',
                                                                            figure = mumbai_timeseries()
                                                                        )

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'delhi-time-map',
                                                                            figure = delhi_timeseries()
                                                                        )

                                                            ],
                                                            className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),



                            html.Div(
                                        [                                
                                            html.H4('WordCloud of Hashtags',className = 'text-center')
                                        ],className = 'row'
                                    ),
                            html.Div(
                                        [
                                                # Column : map
                                              html.Img(
                                                            src = 'data:image/png;base64,{}'.format(encoded_image_1.decode()),
                                                            className='one columns',
                                                            style={
                                                                'height': '450',
                                                                'width': '550',
                                                                'float': 'left',
                                                                # 'position': 'relative',
                                                            },
                                                        ),

                                               html.Img(
                                                            src = 'data:image/png;base64,{}'.format(encoded_image_2.decode()),
                                                            className='one columns',
                                                            style={
                                                                'height': '450',
                                                                'width': '550',
                                                                'float': 'right',
                                                                'position': 'relative',
                                                            },
                                                        ),


                                            ],
                                            className = 'row'
                                    ),

                              html.Div(
                                        [                                
                                            html.H4('Text vs Text+Image',className = 'text-center')
                                        ],className = 'row'
                                    ),

                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'mumbai-text-image',
                                                                            figure = mumbai_textimage()
                                                                        )

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'delhi-text-image',
                                                                            figure = delhi_textimage()
                                                                        )

                                                            ],
                                                            className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),

                              html.Div(
                                        [                                
                                            html.H4('Most Popular tweet',className = 'text-center')
                                        ],className = 'row'
                                    ),


                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                             html.H6('"With #CycloneOckhi expected to make a landfall in Gujarat, \
                                                                I appeal to @BJP4Gujarat Karyakartas to focus on helping people across the state. \
                                                                Our Karyakartas should devote themselves to providing all possible assistance and stand shoulder\
                                                                 to shoulder with fellow citizens" ~ @narendramodi',className = 'text-center')
                                        

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                             html.H6('"Pollution in Delhi-NCR at peak!DelhiSmog compels SriLankan \
                                                                Cricketers to wear mask & NGT to blast DelhiGovernment! PMOPanel gets activated!\
                                                                 #NGT #DelhiSmog #SriLankanCricketers" ~ @mpparimal',className = 'text-center')
                                                            ],className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),

                              html.Div(
                                        [                                
                                            html.H4('Retweets vs Original Tweets',className = 'text-center')
                                        ],className = 'row'
                                    ),


                            html.Div(
                                        [
                                                # Column : map
                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'mumbai-retweet',
                                                                            figure = mumbai_retweet()
                                                                        )

                                                            ],  
                                                            className = 'six columns'
                                                        ),

                                                html.Div(
                                                            [
                                                                dcc.Graph(
                                                                            id = 'delhi-retweet',
                                                                            figure = delhi_retweet()
                                                                        )

                                                            ],
                                                            className = 'six columns'
                                                        ),



                                            ],
                                            className = 'row'
                                    ),










                        ]
                    )










        

app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
})

# Extra Dash styling.
app.css.append_css({
    "external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# JQuery is required for Bootstrap.
app.scripts.append_script({
    "external_url": "https://code.jquery.com/jquery-3.2.1.min.js"
})

# Bootstrap Javascript.
app.scripts.append_script({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
})


if __name__ == '__main__':

	app.run_server(debug = True)
