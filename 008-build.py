#!/usr/bin/env python3
"""
Build index.html with the list of files
"""
import os

if __name__ == '__main__':
    files = os.listdir('.')
    fields = {
      'filelist': '',
      'dataset': '',
      'zip': '',
    }
    for f in sorted(files):
        if f == '.git':
            continue
        appendto = 'filelist'
        if f.startswith('opendata'):
            appendto = 'dataset'
        if f.endswith('.zip'):
            appendto = 'zip'
        fields[appendto] += '<div><a href={0}>{0}</a></div>\n'.format(f)

    with open('index.html.tpl', encoding='utf-8') as template:
        html = template.read()
        for field in fields.keys():
            html = html.replace('{'+field+'}', fields[field])

        with open('index.html', 'w', encoding='utf-8') as out:
            out.write(html)

        print('saved index.html')
