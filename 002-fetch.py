
import json
import os
import urllib

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
    opener = urllib.FancyURLopener()
    opener.addheader('Cookie', cookie)
    stream = opener.open(APIURL, params)
    return stream.read()


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
            data = get_month_data(month, cookie, token)
            # parse, ident json data and save to string
            data = indent(data)
            fw.write(data.encode('utf-8'))
            print('saved %s' % filename)
