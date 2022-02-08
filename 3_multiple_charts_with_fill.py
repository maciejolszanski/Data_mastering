import plotly.graph_objects as go
import csv
from datetime import datetime


filename = 'data/balice_2021.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Only for inforations about columns indexes
    for i, name in enumerate(header_row):
        print(i,name)
    
    place = next(reader)[1]
    
    dates, tmins, tmaxes = [], [], [],
    for row in reader:
        try:
            date = datetime.strptime(row[5], "%Y-%m-%d")
            tmin = (int(row[14])- 32)/1.8 //0.001*0.001 # round to 0.00
            tmax = (int(row[12])- 32)/1.8 //0.001*0.001 # round to 0.00
        except ValueError:
            print(f"no data for {date}")
        else:
            dates.append(date)
            tmins.append(tmin)
            tmaxes.append(tmax)

year = dates[0].year

fig = go.Figure()
fig.add_trace(
    go.Scatter(x=dates, y=tmins, mode='lines', name="minimum temperatures"))
fig.add_trace(
    go.Scatter(x=dates, y=tmaxes, mode='lines',name="maximum temperatures",
    fill='tonexty', fillcolor='rgba(255, 0, 0, 0.1)'))

fig.update_layout(
    title=f"Minimal and Maximal temperatures in {year} in {place}",
    title_font_size = 30,
    xaxis_title="Dates", 
    yaxis_title="Temperature [C]", 
    xaxis_title_font_size=18,
    yaxis_title_font_size=18,
    template='plotly_white'
    )

fig.write_html('min_and_max.html', auto_open=True)