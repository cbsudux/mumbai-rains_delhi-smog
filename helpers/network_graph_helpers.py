import pandas as pd
import plotly
from plotly.graph_objs import *

def mumbai_get_graph():

	df_e = pd.read_csv('edges.csv')


	df_n = pd.read_csv('nodes.csv')

	df_labels = pd.read_csv('labels.csv')

	Xe = []
	for i in df_e['Xe']:
	    Xe.append(i)

	Ye = []

	for i in df_e['Ye']:
	    Ye.append(i)

	Xn = []
	for i in df_n['Xn']:
	    Xn.append(i)

	Yn = []

	for i in df_n['Yn']:
	    Yn.append(i)

	labels = []

	for i in df_labels['labels']:
	    labels.append(i)
	    
	    
	trace1=Scatter(x=Xe,
	               y=Ye,
	               mode='lines',
	               line=Line(color='rgb(210,210,210)', width=1),
	               hoverinfo='none'
	               )
	trace2=Scatter(x=Xn,
	               y=Yn,
	               mode='markers',
	               name='ntw',
	               marker=Marker(symbol='dot',
	                             size=5, 
	                             color='#6959CD',
	                             line=Line(color='rgb(50,50,50)', width=0.5)
	                             ),
	               text=labels,
	               hoverinfo='text'
	               )

	axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
	          zeroline=False,
	          showgrid=False,
	          showticklabels=False,
	          title='' 
	          )

	width=500
	height=500
	layout=Layout(
		title= "Hover to learn more!",  
	    
	    font= Font(size=12),
	    showlegend=False,
	    autosize=False,
	    width=width,
	    height=height,
	    xaxis=XAxis(axis),
	    yaxis=YAxis(axis),          
	    margin=Margin(
	        l=80,
	        r=40,
	        b=85,
	        t=100,
	    ),
	    hovermode='closest',
	    # annotations=Annotations([
	        #    Annotation(
	        #    showarrow=False, 
	        #     text='The Kamada-Kawai layout',  
	        #     xref='paper',     
	        #     yref='paper',     
	        #     x=0,  
	        #     y=-0.1,  
	        #     xanchor='left',   
	        #     yanchor='bottom',  
	        #     font=Font(
	        #     size=14 
	        #     )     
	        #     )
	        # ]),           
	    )

	data=Data([trace1, trace2])
	fig=Figure(data=data, layout=layout)
	return fig


def delhi_getget_graph():

	df_e = pd.read_csv('delhi_edges.csv')


	df_n = pd.read_csv('delhi_nodes.csv')

	df_labels = pd.read_csv('delhi_labels.csv')

	Xe = []
	for i in df_e['Xe']:
	    Xe.append(i)

	Ye = []

	for i in df_e['Ye']:
	    Ye.append(i)

	Xn = []
	for i in df_n['Xn']:
	    Xn.append(i)

	Yn = []

	for i in df_n['Yn']:
	    Yn.append(i)

	labels = []

	for i in df_labels['labels']:
	    labels.append(i)
	    
	    
	trace1=Scatter(x=Xe,
	               y=Ye,
	               mode='lines',
	               line=Line(color='rgb(210,210,210)', width=1),
	               hoverinfo='none'
	               )
	trace2=Scatter(x=Xn,
	               y=Yn,
	               mode='markers',
	               name='ntw',
	               marker=Marker(symbol='dot',
	                             size=5, 
	                             color='#6959CD',
	                             line=Line(color='rgb(50,50,50)', width=0.5)
	                             ),
	               text=labels,
	               hoverinfo='text'
	               )

	axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
	          zeroline=False,
	          showgrid=False,
	          showticklabels=False,
	          title='' 
	          )

	width=500
	height=500
	layout=Layout(
		title= "Zoom in to dive into the network.",  
	 #    font= Font(size=12),
	    showlegend=False,
	    autosize=False,
	    width=width,
	    height=height,
	    xaxis=XAxis(axis),
	    yaxis=YAxis(axis),          
	    margin=Margin(
	        l=80,
	        r=40,
	        b=85,
	        t=100,
	    ),
	    hovermode='closest',
	    # annotations=Annotations([
	    #        Annotation(
	    #        showarrow=False, 
	    #         text='The Kamada-Kawai layout',  
	    #         xref='paper',     
	    #         yref='paper',     
	    #         x=0,  
	    #         y=-0.1,  
	    #         xanchor='left',   
	    #         yanchor='bottom',  
	    #         font=Font(
	    #         size=0
	    #         )     
	    #         )
	    #     ]),           
	    )

	data=Data([trace1, trace2])
	fig=Figure(data=data, layout=layout)
	return fig

