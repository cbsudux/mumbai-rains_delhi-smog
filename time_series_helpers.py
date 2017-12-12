import pandas as pd
import plotly.graph_objs as go
import plotly

def mumbai_timeseries():

	df = pd.read_csv('mumbai_timeseries_data.csv')
	trace_high = go.Scatter(
	    x=df.date,
	    y=df['freq'],
	    name = "freq",
	    line = dict(color = '#17BECF'),
	    opacity = 0.8)

	data = [trace_high]

	layout = dict( 
	    title='Feel free to move the slider around',
        # titlefont = dict(size = 15,color = 'rgb(255,255,255'),

	    
	    
	    yaxis=dict(
	    	linewidth = 1,
                      linecolor = 'rgb(0,0,0)',
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)')),	


	    xaxis=dict(
	    	linewidth = 1,
                      linecolor = 'rgb(0,0,0)',
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)'),	

	        rangeselector=dict(
	            buttons=list([
	                dict(count=1,
	                     label='1d',
	                     step='day',
	                     stepmode='backward'),
	                dict(count=6,
	                     label='1hr',
	                     step='hour',
	                     stepmode='backward'),
	            ])
	        ),
	        rangeslider=dict(autorange = True),
	        type='date'
	    )
	)

	fig = dict(data=data, layout=layout)
	return fig

def delhi_timeseries():
	# TO do : Adjust scale 
# Make bg black

	df = pd.read_csv('delhi_timeseries_data.csv')


	trace_high = go.Scatter(
	    x=df.date,
	    y=df['freq'],
	    name = "freq",
	    line = dict(color = '#17BECF'),
	    opacity = 0.8)

	data = [trace_high]
	
	layout = dict( 

	    # title='Feel free to move the slider around',
     #    titlefont = dict(size = 15,color = 'rgb(255,255,255'),

	    
	    yaxis=dict(
	    	linewidth = 1,
                      linecolor = 'rgb(0,0,0)',
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)')),	


	    xaxis=dict(
	    	linewidth = 1,
                      linecolor = 'rgb(0,0,0)',
                tickfont=dict(
                    size=15,
                    color='rgb(0,0,0)'),	

	        rangeselector=dict(
	            buttons=list([
	                dict(count=1,
	                     label='1d',
	                     step='day',
	                     stepmode='backward'),
	                dict(count=6,
	                     label='1hr',
	                     step='hour',
	                     stepmode='backward'),
	            ])
	        ),
	        rangeslider=dict(autorange = True),
	        type='date'
	    )
	)
	fig = dict(data=data, layout=layout)
	return fig





