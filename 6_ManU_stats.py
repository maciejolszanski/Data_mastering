import json
import plotly.graph_objects as go
import numpy as np

filename = 'data/football_data.json'

with open(filename) as f:
    full_dict = json.load(f)
    
    # for key, value in full_dict['response'].items():
    #     print(key, value, '\n')

fixtures = full_dict['response']['fixtures']
wins = [win for win in fixtures['wins'].values()]
loses = [loss for loss in fixtures['loses'].values()]
draws = [draw for draw in fixtures['draws'].values()]

team = full_dict['response']['team']['name']
season = full_dict['parameters']['season']

# matrix with columns: home, away, total
games = np.array([wins, draws, loses])
wins_percent = games[:,0]/games[:,2] * 100
loses_percent = games[:,1]/games[:,2] * 100

fig = go.Figure()

labels = ['wins', 'draws', 'loses']
fig.add_trace(
    go.Bar(
        x=labels,
        y=wins_percent,
        name='home',
        text=np.round(wins_percent, 2),
        textfont_size=20
        )
    )
fig.add_trace(
    go.Bar(x=labels,
        y=loses_percent,
        name='away',
        text=np.round(loses_percent, 2),
        textfont_size=20
        )
    )
fig.update_layout(
    title=f"{team} stats in {season}",
    title_font_size=24,
    barmode='relative',
    )

fig.write_html('charts/football.html', auto_open=True)