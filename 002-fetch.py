#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Читаем сессию, токен, список месяцев, и тащим страницы
с даннымм по месяцам.
"""

import json
import os
from urllib.request import FancyURLopener

APIURL = 'http://115.xn--90ais/api/problem/getlist'


def indent(jsondata):
    try:
        data = json.loads(jsondata)
    except ValueError:
        open('.002-fetch-error', 'wb').write(jsondata.encode('utf-8'))
        print('error loading json, data saved to .002-fetch-error.txt')
        raise
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


def get_month_data(month, cookie, token):
    params = 'date={}&_token={}'.format(month, token)
    opener = FancyURLopener()
    opener.addheader('Cookie', cookie)
    stream = opener.open(APIURL, params)
    return stream.read().decode('utf-8')


if __name__ == '__main__':
    with open('002-in-creds.txt', encoding='utf-8') as fd:
        cookie = fd.readline().strip()
        token = fd.readline().strip()
        months = fd.read().strip().split('\n')

    for month in months:
        filename = '003-in-%s.json' % month
        if os.path.exists(filename):
            print('skipping {}'.format(filename))
            continue
        print('saving %s' % filename, flush=True)
        with open(filename, 'w', encoding='utf-8') as fw:
            data = get_month_data(month, cookie, token)
            # parse, ident json data and save to string
            data = indent(data)
            fw.write(data)
