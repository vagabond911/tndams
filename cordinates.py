import csv
import pprint
import re

def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    return dd

def getdam(damfile):
    with open(damfile, 'r') as f:
          reader = csv.DictReader(f)
          dict_list = []
          for line in reader:
              dict_list.append(line)

    keys = ["NAME OF DAM", "District", "Longitude of dam", "Latitude of dam ", "River"]
    finallist = []

    for damdict in dict_list:
        new = dict((key, value) for key, value in damdict.items() if key in keys)
        [d, m, s, x] = re.split('[°\'"]+', new['Longitude of dam'])
        new['Longitude of dam'] = dms2dd(d, m, s)
        [d, m, s, x] = re.split('[°\'"]+', new['Latitude of dam '])
        new['Latitude of dam '] = dms2dd(d, m, s)
        finallist.append(new)

    return (finallist)
