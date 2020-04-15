import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")

lat = list(df["LAT"])
lon = list(df["LON"])
elv = list(df["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "blue"
    else:
        return "red"


m = folium.Map(location=[38.379155, -98.355610],zoom_start=6,tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon,elv):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m", icon=folium.Icon(color_producer(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding = "utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"]<10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

m.add_child(fgv)
m.add_child(fgp)

m.add_child(folium.LayerControl())

m.save("Map1.html")
