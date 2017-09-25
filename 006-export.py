#!/usr/bin/env python

import os

def build_all_csv():
    """ Build one file with all data """
    alldataname = 'opendata-115-all.csv'
    with open(alldataname, 'wb') as acf:
        head = False  # write CSV header from the first file processed
        for f in sorted(os.listdir('.')):
            if f.endswith('.csv') and f.startswith('opendata-115-2'):
                with open(f, 'rb') as scf:
                    header = scf.readline()
                    if not head:
                        acf.write(header)
                        head = True
                    else:
                        pass  # skp header for subsequent files
                    for line in scf:
                        acf.write(line)
    print('saved {}'.format(alldataname))

if __name__ == '__main__':
    build_all_csv()

