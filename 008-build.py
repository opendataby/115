"""
Build index.html with the list of files
"""
import os

if __name__ == '__main__':
    files = os.listdir('.')
    fields = {'filelist': ''}
    for f in files:
        if f == '.git':
            continue
        fields['filelist'] += '<div><a href={0}>{0}</a></div>\n'.format(f)

    with open('index.html.tpl', 'rb') as template:
        html = template.read()
        
        with open('index.html', 'wb') as out:
            out.write(html.format(**fields))

        print('saved index.html')
