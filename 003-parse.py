# -*- coding: utf-8 -*-
"""
https://github.com/opendataby/city-dashboard/issues/53

Example:

    "items": {
        "68036": {
            "address": "рядом с улица Максима Богдановича, 143", 
            "category": {
                "icon": "6", 
                "id": "25", 
                "parent_id": "6"
            }, 
            "crm_create_at": "2017-04-01", 
            "crm_date_planned": "2017-04-03", 
            "date_create": "1 апреля 0:16", 
            "date_planned": "03.04.2017", 
            "href": "/problem/68036", 
            "id": "68036", 
            "lat": "53.92498779", 
            "lng": "27.57044029", 
            "photo": {
                "after": [], 
                "before": []
            }, 
            "rating": "0", 
            "status": "3", 
            "user": {
                "id": "6635", 
                "last_name": "Евгений", 
                "middle_name": "", 
                "name": "Евгений"
            }
        }, 
        "68037": {

Possible status values:

    > findstr "status" *.json | cut -d":" -f 2,3,4 | "C:\Program Files\Dev\Git\usr\bin\sort.exe" -u

        "status": "1",
        "status": "3",
        "status": "4",
        "status": "5",
        "status": "7",
"""

import csv
import json
import os
from collections import OrderedDict as odict


def fields(ob):
    if type(ob) == dict:
        for f in ob.keys():
            print(f)
    else:
        for f in dir(ob):
            if not f.startswith('__'):
                print(f)


def json2csv(inname, outname):
    data = json.load(open(inname, 'r'))
    with open(outname, 'wb') as outcsv:
        #outcsv.write('# https://github.com/opendataby/city-dashboard/issues/53\n')
        #outcsv.write('# \n')
        names = ['id', 'category', 'author', 'name', 'address', 'status', 'opened', 'planned']
        writer = csv.DictWriter(outcsv, fieldnames=names)
        writer.writeheader()
        for issue in data['items']:
            item = data['items'][issue].copy()
            
            #fields(item['category'])
            created = item['date_create'].split()[2]  # "1 апреля 0:16"
            authorid = item['user']['id'] if item['user'] else 0
            name = item['user']['name'].encode('utf-8').strip() if item['user'] else ''
            try:
                entry = odict([
                  ('id', item['id']),
                  ('category', '{parent_id}.{id}'.format(**item['category'])),
                  ('author', authorid),
                  ('name', name),
                  ('address', item['address'].encode('utf-8').strip()),
                  ('status', item['status']),
                  ('opened', item['crm_create_at']+" "+created),
                  ('planned', item['crm_date_planned']),
                ])
            except TypeError:
                print('Error: file {}, issue {}'.format(inname, item['id']))
                raise

            """
             "address": "рядом с улица Максима Богдановича, 143", 
             "crm_create_at": "2017-04-01", 
             "crm_date_planned": "2017-04-03", 
             "date_create": "1 апреля 0:16", 
             "date_planned": "03.04.2017", 
             "lat": "53.92498779", 
             "lng": "27.57044029", 
             "photo": {
                 "after": [], 
                 "before": []
             }, 
             "rating": "0", 
             "status": "3", 
             "user": {
                 "id": "6635", 
                 "last_name": "Евгений", 
                 "middle_name": "", 
                 "name": "Евгений"
             }
             """

            writer.writerow(entry)
            #sys.exit()


if __name__ == '__main__':
    #for name in ['003-in-2017-04-01.json']:
    for name in os.listdir('.'):
        # 003-in-2017-04-01.json
        if name.startswith('003-in-') and name.endswith('.json'):
            month = name[7:-5]
            json2csv(name, 'opendata-115-%s.csv' % month)
