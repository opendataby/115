python2 001-order.py -f
python2 002-fetch.py
python2 003-parse.py
python2 006-export.py

zip "dataset-115.bel-$(date +'%Y%m%d-%H%M%S').zip" opendata*

python2 008-build.py
