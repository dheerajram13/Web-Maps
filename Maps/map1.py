import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")          # opening file using pandas
lat = list(data["LAT"])                           # storing lat in a list
lon = list(data["LON"])                            # storing lat in a list
elev = list(data["ELEV"])                           # storing elevation in a list

def color_producer(elevation):                   # function to mark the coordinates with respect to their elevation
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")              # volcano groups in US

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")            # fill colors according to the  population  of the world
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),style_function=lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 10000000
else 'orange' if 10000000<= x["properties"]["POP2005"] <= 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
