import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore structure of the data
filename = './sample_usgs_data.json'
with open(filename) as f:
	data = json.load(f) # loads JSON as a giant dictionary

mags, lons, lats = [], [], []
all_eq_dicts = data['features']
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig={'data' : data, 'layout' : my_layout}
offline.plot(fig,filename='global_earthquakes.html')