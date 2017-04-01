
import os
import urllib

APIURL = 'http://115.xn--90ais/api/problem/getlist'


def escape2unicode(string):
    """
    Convert from \u043c\u0430\u0440 to unicode object to utf-8
    """
    return string.decode('unicode-escape').encode('utf-8')

def get_month_data(month, cookie, token):
    params = 'date={}&_token={}'.format(month, token)
    opener = urllib.FancyURLopener()
    opener.addheader('Cookie', cookie)
    stream = opener.open(APIURL, params)
    return escape2unicode(stream.read())


if __name__ == '__main__':
    with open('002-in-creds.txt', 'rb') as fd:
        cookie = fd.readline().strip()
        token = fd.readline().strip()
        months = fd.read().strip().split('\n')

    for month in months:
        filename = '003-in-%s.json' % month
        if os.path.exists(filename):
            continue
        with open(filename, 'wb') as fw:
            fw.write(get_month_data(month, cookie, token))
            print('saved %s' % filename)
