import plotly.graph_objects as go
import plotly.express as px
import numpy as np


x_1 = np.arange(0,100,1)
y_1 = [2*x**2 - 1/2*x for x in x_1]

# Method 1
data_dict = {'x': x_1, 'y': y_1,}
fig_1 = px.line(data_dict, title='My test figure', x=x_1, y=y_1)
fig_1.write_html('charts/plot_1.html', auto_open=True)

# Method 2
fig_2 = go.Figure(
    data=[go.Scatter(x=x_1, y=y_1, mode='lines')],
    layout=go.Layout(title="My test figure",xaxis_title='x', yaxis_title='y')
    )

fig_2.write_html('charts/plot_2.html', auto_open=True)
