python 001-order.py -f
python 002-fetch.py
python 003-parse.py
zip "dataset-115.bel-$(date +'%Y%m%d-%H%M%S').zip" opendata*
python 008-build.py
