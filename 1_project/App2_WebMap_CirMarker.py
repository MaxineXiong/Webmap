import folium

#build a base map
map2 = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = 'Stamen Terrain') #tiles is the background style of the map

#Create a Feature Group collecting Volcano Data for markers
fg_cmk = folium.FeatureGroup(name = 'Volcano')

import pandas as pd
VolData = pd.read_csv('Volcanoes.txt')

def color_marker(elevation):
    if elevation > 3000:
        return 'purple'
    elif elevation > 1000:
        return 'orange'
    else:
        return 'blue'

for i in range(0, len(VolData)):
    fg_cmk.add_child(folium.CircleMarker(location = [VolData.LAT[i], VolData.LON[i]],
                                        radius = 15,  #radius: size of markers
                                        popup = folium.Popup(str(VolData.ELEV[i]) + 'm', parse_html = True),
                                        fill = True, fill_color = color_marker(VolData.ELEV[i]), color = 'grey', fill_opacity = 0.8))  #color: edgecolor #fill_opacity: transparency of markers

#Create a Feature Group collecting Population Data for polygon
fg_plg = folium.FeatureGroup(name = 'Population')

#the fill color of polygon will vary according to popluation by country, so define a variable 'country' after lambda
fg_plg.add_child(folium.GeoJson(data = open('world.json', encoding = 'utf-8-sig').read(), #use encoding = 'utf-8-sig' to stop the return of whole .json file in terminal
                                style_function = lambda country: {'fillColor':'red' if country['properties']['POP2005'] > 20000000
                                                                               else 'yellow' if country['properties']['POP2005'] > 10000000
                                                                               else 'green',
                                                                  'fillOpacity':0.5, 'color':'black', 'weight':1}))  #weight: weight of edgecolor

#add 2 feature groups to map1
map2.add_child(fg_cmk)    #.add_child: can only add ONE child at a time
map2.add_child(fg_plg)

#add layer control to Map1
map2.add_child(folium.LayerControl())

#save map1 as '.html' link
map2.save('Map2.html')
