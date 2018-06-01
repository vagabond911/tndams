import csv
import pprint
from contextlib import closing
import codecs
import re
import requests
import folium

def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    return dd

def getdam():
    url = 'https://tn.data.gov.in/node/5241/download'
    dict_list = []
    with closing(requests.get(url, stream=True)) as r:
        reader = csv.DictReader(codecs.iterdecode(r.iter_lines(), 'utf-8',  errors='ignore'))
        for line in reader:
            dict_list.append(line)

    keys = ["NAME OF DAM", "District", "Longitude of dam", "Latitude of dam ", "River"]
    finallist = []

    for damdict in dict_list:
        new = dict((key, value) for key, value in damdict.items() if key in keys)

        [dm, s, x] = re.split('[°\'"]+', new['Longitude of dam'])
        d = int(int(dm) / 100)
        m = int((int(dm) % 100))
        new['Longitude of dam'] = dms2dd(d, m, s)

        [dm, s, x] = re.split('[°\'"]+', new['Latitude of dam '])
        d = int(int(dm) / 100)
        m = int((int(dm)%100))
        new['Latitude of dam '] = dms2dd(d, m, s)

        finallist.append(new)

    return (finallist)

#print(help(folium.map))

map1 = folium.Map(location=[10.9, 77.519],zoom_start=7,
tiles='mapboxbright', width=1020, height=600)

fgdam = folium.FeatureGroup(name = "TN Dams")
dams = getdam()

for dam in dams:
    fgdam.add_child(folium.Marker(location=[dam['Longitude of dam'], dam['Latitude of dam ']], popup=dam["NAME OF DAM"],
                                  icon=folium.Icon(icon='tint', icon_color='lightblue', color='darkblue')))

map1.add_child(fgdam)
map1