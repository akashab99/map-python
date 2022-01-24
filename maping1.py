from cgitb import grey
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])


html = """<h4>Volcano information:</h4>
Height: %s m
"""
def color_produce(elevation):
     if elevation <1000:
         return 'purple'
     elif 1000<= elevation <3000:
          return 'red'
     else:
          return 'green' 

map = folium.Map(location=[13.107770194956931, 80.09736606793335],zoom_start=6, tiles="Stamen terrain")  


fgp= folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'yellow' if x ['properties']['POP2005']<10000000
else 'green' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))

fgv = folium.FeatureGroup(name="Volcanoes")

for lt , ln , el in  zip(lat, lon,elev):
     iframe = folium.IFrame(html=html % str(el), width=200, height=100)
     fgv.add_child(folium.CircleMarker(location=[ lt, ln ],radius=5,popup=folium.Popup(iframe,str(el)+"m"), tooltip= 'Click here',
     fill_color=color_produce(el),color = 'grey', fill_opacity=0.7,icon=folium.Icon(color= color_produce(el))))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map_html_popup_simple.html")

map.save("Map1.html")
