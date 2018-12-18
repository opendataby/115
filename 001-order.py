#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Инструментарий по скрейпингу/парсингу на примере 115.бел
на чистом Python. 115.бел не open source, PHP + Laravel.

Для городской панели и не только
https://github.com/opendataby/city-dashboard/issues/53

"""

import os
import re
import sys
from urllib.request import urlopen


# http://115.бел/map
URL = 'http://115.xn--90ais/map'


def rewrite(filename, content):
    with open(filename, 'w', encoding='utf-8') as fd:
        fd.write(content)
        print('saved %s' % fd.name)


def get_page(url, cachefile, force=False):
    """
    Fetch page and cookie from URL if local cachefile does not exist
    """
    if os.path.exists(cachefile) and not force:
        print('using cached ' + cachefile + ' (-f to force update)')
        with open(cachefile, encoding='utf-8') as fc:
            cookie = fc.readline().strip()
            return fc.read(), cookie
    else:
        req = urlopen(url)
        for line in str(req.headers).splitlines():
            if line.startswith('Set-Cookie'):
                cookie = line.split(': ', 1)[1]
        output = req.read().decode('utf-8')
        rewrite(cachefile, cookie+'\n'+output)
        return output, cookie


def get_months(content):
  """ Get (parse) list of months from content """
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)"')
  return remonth.findall(content)

def calc_months(curdate):
  """ Calculate months up to curdate from hardcoded date """
  hardcoded = '2015-11-01'
  date = [int(i) for i in hardcoded.split('-')]
  res = []
  while date <= [int(i) for i in curdate.split('-')]:
    res.append('{:04d}-{:02d}-{:02d}'.format(*date))
    y, date[1] = divmod(date[1]+1, 13)
    if y:
      date[1] = 1
      date[0] += 1
  return res

def get_cur_month(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)" checked="checked"')
  return remonth.findall(content)[0]  # 2017-03-01

def get_token(content):
  return re.findall('_token"\s+value="(\w+)"', content)[0]


if __name__ == '__main__':
    force = False
    if '-f' in sys.argv:
        force = True

    content, cookie = get_page(URL, '001-in-seed.txt', force)

    curmon = get_cur_month(content)
    #months = get_months(content)
    months = calc_months(curmon)
    rest = sorted(list(months))
    rest.remove(curmon)

    # next step is fetch, which needs token, laravel_session cookie
    # and list of months
    token = get_token(content)
    # list of months includes current (incomplete) month
    rewrite('002-in-creds.txt', cookie+'\n'+token+'\n'+'\n'.join(months))
