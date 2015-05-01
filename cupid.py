__author__ = 'OliPicard'
import csv
import json
import sys
import requests

'''a csv to json converter written for the UKStationLive schema
run this tool via cmd> cupid.py station.csv
Thank you to the following
'''

def cupid():
    csv_file = requests.get('http://www.nationalrail.co.uk/static/documents/content/station_codes.csv', stream=True)
    if csv_file.status_code == requests.codes.ok:
        print("Grabbing file from National Rail")
        with open('station_codes.csv', 'wb') as e:
            for chunk in csv_file.iter_content(chunk_size=1024):
                if chunk:
                    e.write(chunk)
                    e.flush()
    try:
        t = open('station_codes.csv', 'r')
    except IOError:
        print('Unable to get data. delete the file and try again!')
        sys.exit()
    headers = ['Station Name', 'Code']
    csv_reader = csv.DictReader(t, headers)
    json_filename = 'station.json'
    print('Saving the file', json_filename)
    jsonf = open(json_filename, 'w')
    data = {r['Station Name']: r['Code'] for r in csv_reader}
    redata = json.dumps(data, indent=4, sort_keys=True)
    jsonf.write(redata)
    e.close()
    jsonf.close()

if __name__ == "__main__":
    cupid()