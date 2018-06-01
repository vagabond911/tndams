import folium
import cordinates

#print(help(folium.map))

map1 = folium.Map(location=[10.9, 77.519],zoom_start=7,
tiles='mapboxbright', width=1020, height=600)

fgdam = folium.FeatureGroup(name = "TN Dams")
dams = cordinates.getdam("TNDAMSLIST_1.csv")

for dam in dams:
    fgdam.add_child(folium.Marker(location=[dam['Longitude of dam'], dam['Latitude of dam ']], popup=dam["NAME OF DAM"],
                                  icon=folium.Icon(icon='tint', icon_color='lightblue', color='darkblue')))

map1.add_child(fgdam)
map1.save("maps.html")

