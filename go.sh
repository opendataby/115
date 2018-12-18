python3 001-order.py -f
python3 002-fetch.py
python3 003-parse.py
python3 006-export.py

zip "dataset-115.bel-$(date +'%Y%m%d-%H%M%S').zip" opendata*

python3 008-build.py
