import plotly.graph_objects as go
import csv
import calendar
from datetime import datetime


def extract_rain_daily(filename):

    with open(filename) as f:
        reader = csv.reader(f)
        title_row = next(reader)

        # for i, name in enumerate(title_row):
        #     print(i, name)
        
        # format the name from PLACE, PL to Place, PL
        place_string = next(reader)[1].split(',')
        place = ','.join([place_string[0].title(), place_string[1]])

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
fig = go.Figure()
fig.add_trace(
    go.Pie(labels=months, values=rains_monthly,
           marker_line_color='#000000',
           marker_line_width=2,
           textfont_size=20,
           )
    )
fig.update_layout(
    title=f'Rains in the {place} in {year}',
    title_font_size=24,
)

fig.write_html('charts/pie.html', auto_open=True)