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


def rewrite(filename, content):
    with open(filename, 'wb') as fd:
        fd.write(content)
        print('saved %s' % fd.name)

def get_page(url, cachefile, force=False):
    """
    Fetch page and cookie from URL if local cachefile does not exist
    """
    if os.path.exists(cachefile) and not force:
        with open(cachefile, 'rb') as fc:
            cookie = fc.readline().strip()
            return fc.read(), cookie
    else:
        req = urllib.urlopen(url)
        for line in str(req.headers).splitlines():
            if line.startswith('Set-Cookie'):
                cookie = line.split(': ', 1)[1]
        output = req.read()
        rewrite(cachefile, cookie+'\n'+output)
        return output, cookie

def escape2unicode(string):
    """
    Convert from \u043c\u0430\u0440 to unicode object to utf-8
    """
    return string.decode('unicode-escape').encode('utf-8')


def get_months(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)"')
  return remonth.findall(content)

def get_cur_month(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)" checked="checked"')
  return remonth.findall(content)[0]

def get_token(content):
  return re.findall('_token"\s+value="(\w+)"', content)[0]


if __name__ == '__main__':
    content, cookie = get_page(URL, '001-in-seed.txt')

    months = get_months(content)
    curmon = get_cur_month(content)
    rest = list(months)
    rest.remove(curmon)

    # next step is fetch, which needs token, laravel_session cookie
    # and list of months
    token = get_token(content)
    rewrite('002-in-creds.txt', cookie+'\n'+token+'\n'+'\n'.join(months))

    apiurl = 'http://115.xn--90ais/api/problem/getlist'
    params = 'date={}&_token={}'.format(curmon, token)
    opener = urllib.FancyURLopener()
    opener.addheader('Cookie', cookie)
    stream = opener.open(apiurl, params)
    
    data = stream.read()
    with open(curmon, 'wb') as fw:
        fw.write(escape2unicode(data))
