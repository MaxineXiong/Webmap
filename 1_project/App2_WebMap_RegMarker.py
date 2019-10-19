import folium

#build a base map
map1 = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = 'Stamen Terrain') #tiles is the background style of the map

#Create a Feature Group collecting Volcano Data for markers
fg_mk = folium.FeatureGroup(name = 'Volcano')

import pandas as pd
VolData = pd.read_csv('Volcanoes.txt')

for i in range(0, len(VolData)):
    fg_mk.add_child(folium.Marker(location = [VolData.LAT[i], VolData.LON[i]],
                                  popup = folium.Popup(str(VolData.ELEV[i]) + 'm', parse_html = True),
                                  icon = folium.Icon(color = 'green', icon_color = 'red')))

#Create a Feature Group collecting Population Data for polygon
fg_plg = folium.FeatureGroup(name = 'Population')

#the fill color of polygon will vary according to popluation by country, so define a variable 'country' after lambda
fg_plg.add_child(folium.GeoJson(data = open('world.json', encoding = 'utf-8-sig').read(), #use encoding = 'utf-8-sig' to stop the return of whole .json file in terminal
                                style_function = lambda country: {'fillColor':'red' if country['properties']['POP2005'] > 20000000
                                                                               else 'yellow' if country['properties']['POP2005'] > 10000000
                                                                               else 'green'}))

#add 2 feature groups to map1
map1.add_child(fg_mk)    #.add_child: can only add ONE child at a time
map1.add_child(fg_plg)

#add layer control to Map1
map1.add_child(folium.LayerControl())

#save map1 as '.html' link
map1.save('Map1.html')
