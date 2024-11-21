from pathlib import Path
import json
import plotly.express as px

from pathlib import Path
import json

#read data as a string and convert to a Python object
path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/eq_data/eq_data_30_day_m1.geojson')
#read the data as a string
contents = path.read_text(encoding='utf-8')
#use json.loads() to convert it into a Python object
all_eq_data = json.loads(contents)

#Create a more readable version of the data file
path = Path('C:/Users/ymarv/OneDrive/Desktop/python/Chapter_16/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents, encoding='utf-8')

#examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']
meta_data_dict = all_eq_data['metadata']
print(len(all_eq_dicts))

mags= []
lons = []
lats = []
eq_titles = []

title = meta_data_dict['title']

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

#scatter_geo allows us to overlay a scatterplot of geographic data on a map
fig = px.scatter_geo(lat=lats, lon=lons, title=title, 
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'magnitute'},
                     projection='natural earth',
                     hover_name=eq_titles )

fig.write_html('world_eq.html', auto_open=True)