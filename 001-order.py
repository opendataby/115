# -*- coding: utf-8 -*-

import os
import re
import urllib


def get_page_contents(url, cachefile, force=False):
    """
    Fetch page from URL if local cachefile does not exist
    """
    if os.path.exists(cachefile) and not force:
        return open(cachefile, 'rb').read()
    else:
        output = urllib.urlopen(url).read()
        with open(cachefile, 'wb') as fw:
            fw.write(output)
        return output


def get_months(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)"')
  return remonth.findall(content)

def get_cur_month(content):
  remonth = re.compile('name="month-filter" value="(\d\d\d\d-\d\d-\d\d)" checked="checked"')
  return remonth.findall(content)[0]


if __name__ == '__main__':
    # http://115.бел/map
    url = 'http://115.xn--90ais/map'
    content = get_page_contents(url, '001-seed.txt')

    months = get_months(content)
    curmon = get_cur_month(content)
    rest = list(months)
    rest.remove(curmon)

    print('current month: ' + curmon)
    print('all months: ' + ', '.join(months))
    print('all months: ' + ', '.join(months))
