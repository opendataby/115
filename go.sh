python2 001-order.py -f
python2 002-fetch.py
python2 003-parse.py

head -1 $(ls opendata-115-2* | head -1) > opendata-115-all.csv
tail -n+2 -q opendata-115-2* >> opendata-115-all.csv

zip "dataset-115.bel-$(date +'%Y%m%d-%H%M%S').zip" opendata*

python2 008-build.py
