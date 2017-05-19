"""
Build index.html with the list of files
"""
import os

if __name__ == '__main__':
    files = os.listdir('.')
    fields = {
      'filelist': '',
      'dataset': '',
    }
    for f in files:
        if f == '.git':
            continue
        appendto = 'filelist'
        if f.startswith('opendata'):
            appendto = 'dataset'
        fields[appendto] += '<div><a href={0}>{0}</a></div>\n'.format(f)

    with open('index.html.tpl', 'rb') as template:
        html = template.read()
        for field in fields.keys():
            html = html.replace('{'+field+'}', fields[field])
        
        with open('index.html', 'wb') as out:
            out.write(html)

        print('saved index.html')
