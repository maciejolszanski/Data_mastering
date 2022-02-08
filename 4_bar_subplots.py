from matplotlib.pyplot import xticks
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import csv
import numpy as np
from datetime import datetime
import calendar


def extract_rain_daily(filename):

    with open(filename) as f:
        reader = csv.reader(f)
        title_row = next(reader)

        # for i, name in enumerate(title_row):
        #     print(i, name)
        
        place = next(reader)[1]

        dates, rains = [], []
        for row in reader:
            try:
                date = datetime.strptime(row[5], '%Y-%m-%d')
                rain = float(row[6])
            except ValueError:
                print(f'No data for {date}')
                dates.append(date)
                rains.append(0)
            else:
                dates.append(date)
                rains.append(rain)
        
    return dates, rains, place

def convert_daily_to_monthly(dates, values):

    vals_monthly = []
    for month_num in range(1,13):
        month_values = 0
        for date in dates:
            if date.month == month_num:
                month_values += values[dates.index(date)]

        month_values = month_values //0.01/100
        vals_monthly.append(month_values) 
        
    return vals_monthly


# DATA PREPARATION
filename = 'data/balice_2021.csv'

dates, rains_daily, place = extract_rain_daily(filename)
year = dates[0].year

months = calendar.month_name[1:]
rains_monthly = convert_daily_to_monthly(dates, rains_daily)



# DATA VISUALISATION
fig = make_subplots(rows=2, cols=1)

fig.add_trace(
    go.Bar(x=dates, y=rains_daily, name='rains daily',),
    row=1, 
    col=1,
    )

fig.add_trace(
    go.Bar(x=months, y=rains_monthly, name='rains monthly'),
    row=2,
    col=1,
    )

fig.update_layout(
    title=f'Rains in {place} in {year}',
    title_font_size=24,
    template='plotly_white',
    )

fig.update_xaxes(title='dates',ticktext=dates, row=1, col=1)
fig.update_xaxes(ticktext=months, row=2, col=1)

fig.write_html('charts/rains.html', auto_open=True)