import plotly
from plotly import graph_objs

plotly.offline.init_notebook_mode(connected=True)

trace0 = graph_objs.Scatter(
    text=list(map(lambda movie: movie['title'],movies)),
    x=list(map(lambda movie: movie['budget'],movies)),
    y=list(map(lambda movie: movie['revenue'],movies)),
    mode="markers",
)



layout= graph_objs.Layout(
    title= 'Movie Spending and Revenue',
    xaxis= dict(
        title= 'Movie Budget',
        zeroline = True,
        range=[30000000, 200000000]
    ),
    yaxis=dict(
        title= 'Movie Revenue',
        zeroline = True,
        range=[0, 400000000]
    ),
    showlegend= False
)
plotly.offline.iplot(dict(data=[trace0], layout=layout))
