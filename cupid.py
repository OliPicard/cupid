__author__ = 'OliPicard'
import csv
import json
import sys


'''a csv to json converter written for the UKStationLive schema
run this tool via cmd> cupid.py station.csv
Thank you to the following
'''



def cupid(file):
    csv_file = file[0]
    print("Opening the CSV file.")
    try:
        e = open(csv_file, 'r')
    except IOError:
        print('It seems that the file hasnt been located')
        sys.exit()
    headers = ['Station Name', 'Code']
    csv_reader = csv.DictReader(e, headers)
    json_filename = 'station.json'
    print('Saving the file', json_filename)
    jsonf = open(json_filename, 'w')
    data = json.dumps({r['Station Name']: r['Code'] for r in csv_reader})
    jsonf.write(data)
    e.close()
    jsonf.close()

if __name__ == "__main__":
    cupid(sys.argv[1:])