# -*- coding: utf-8 -*-
"""
Инструментарий по скрейпингу/парсингу на примере 115.бел
на чистом Python. 115.бел не open source, PHP + Laravel.

Для городской панели и не только
https://github.com/opendataby/city-dashboard/issues/53

"""

import os
import re
import urllib


# http://115.бел/map
URL = 'http://115.xn--90ais/map'

def get_page_contents(url, cachefile, force=False):
    """
    Fetch page from URL if local cachefile does not exist
    """
    if os.path.exists(cachefile) and not force:
        return open(cachefile, 'rb').read()
    else:
        req = urllib.urlopen(url)
        output = req.read()
        with open(cachefile, 'wb') as fw:
            fw.write(output)
        return output


def get_months(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)"')
  return remonth.findall(content)

def get_cur_month(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)" checked="checked"')
  return remonth.findall(content)[0]

def get_token(content):
  return re.findall('_token"\s+value="(\w+)"', content)[0]


if __name__ == '__main__':
    content = get_page_contents(URL, '001-seed.txt')

    months = get_months(content)
    curmon = get_cur_month(content)
    rest = list(months)
    rest.remove(curmon)

    print('current month: ' + curmon)
    print('all months: ' + ', '.join(months))

    token = get_token(content)

    apiurl = 'http://115.xn--90ais/api/problem/getlist'
    params = 'date={}&_token={}'.format(curmon, token)
    stream = urllib.urlopen(apiurl, params)
    data = stream.read()
    with open(curmon, 'wb') as fw:
        fw.write(data)
