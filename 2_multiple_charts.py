import plotly.graph_objects as go
import numpy as np

x_1 = np.arange(0,100,0.1)
x_2 = np.arange(0,100,0.1)

y_1 = [x**2 for x in x_1]
y_2 = [-x**2 + 10000 for x in x_2]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_1, y=y_1, name='Function 1'))
fig.add_trace(go.Scatter(x=x_2, y=y_2, name='Function 2'))

fig.update_layout(title="Double chart", xaxis_title='x', yaxis_title='y',
    template='plotly_white')

fig.write_html('multiple.html', auto_open=True)