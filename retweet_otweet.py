import plotly
import plotly.graph_objs as go

    
def mumbai_retweet():
    data = [go.Bar(
                x=['retweets','original tweets'],
                y=[9044,965],
                marker=dict( color = ['#1dcaff','#ff4f81'])
        )]

    layout = go.Layout(
                    # title = 'Text vs Text+Image<br>(Hover for metrics)',
            # titlefont = dict(size = 20,color = 'rgb(255,255,255'),
           xaxis=dict(linewidth = 1,
                      linecolor = 'rgb(0,0,0)',
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)'
                    
                )
           ),
            yaxis=dict( linecolor = 'rgb(0,0,0)',linewidth = 1,
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)'
                    
                )
        ))
        
    fig = go.Figure(data=data, layout=layout)
    return fig 


def delhi_retweet():

    data = [go.Bar(
                x=['retweets','original tweets'],
                y=[4341,2557],
                marker=dict( color = ['#1dcaff','#ff4f81'])
        )]
    layout = go.Layout(
                    # title = 'Text vs Text+Image<br>(Hover for metrics)',
            # titlefont = dict(size = 20,color = 'rgb(255,255,255'),
           xaxis=dict(linewidth = 1,
                      linecolor = 'rgb(0,0,0)',
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)'
                    
                )
           ),
            yaxis=dict( linecolor = 'rgb(0,0,0)',linewidth = 1,
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)'
                    
                )
        ))

    fig = go.Figure(data=data, layout=layout)

    return fig