import plotly.express as px
from pathlib import Path
import csv

path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/eq_data/world_fires_1_day.csv')

lines = path.read_text().splitlines()

reader = csv.reader(lines)

header_row = next(reader)


#getting the data
lats = []
lons = []
brightness = []

for row in reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        print("Error with data")
    else: 
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)


title = "World Forest Fire"
#plotting the data
fig = px.scatter_geo(
    lat=lats, 
    lon=lons, 
    title=title, 
    color=brightness, 
    color_continuous_scale='Viridis', 
    labels={'color':'brightness'}, 
    projection='natural earth'
)
fig.write_html('world_fire.html', auto_open=True)