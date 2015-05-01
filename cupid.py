__author__ = 'OliPicard'
import csv
import json
import sys
from io import StringIO
import requests

'''a csv to json converter written for the UKStationLive schema
simply run the tool to get the station.json output.
Thank you to the following
excalibur (for his streaming data save copy)
diminonten (for his memory version)
'''

def cupid():
    response = requests.get('http://www.nationalrail.co.uk/static/documents/content/station_codes.csv')
    if response.status_code == requests.codes.ok:
        print("Grabbing file from National Rail")
        csv_file = StringIO(response.content.decode())
    headers = ['Station Name', 'Code']
    csv_reader = csv.DictReader(csv_file, headers)
    json_filename = 'station.json'
    print('Saving the file', json_filename)
    jsonf = open(json_filename, 'w')
    data = {r['Station Name']: r['Code'] for r in csv_reader}
    redata = json.dumps(data, indent=4, sort_keys=True)
    jsonf.write(redata)
    jsonf.close()

if __name__ == "__main__":
    cupid()