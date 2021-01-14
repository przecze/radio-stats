#!/usr/bin/python3
from bs4 import BeautifulSoup as Soup
import requests
from datetime import datetime
import sys
import os

values = [str(datetime.now())]
for url in ("https://patronite.pl/radionowyswiat", "https://patronite.pl/radio357"):
    document = Soup(requests.get(url).text, 'lxml')
    for element_id in ('stats-patrons', 'stats-monthly', 'stats-total'):
        value = document.find(attrs={'id': element_id}).text
        value = str(value.replace(' ',''))
        values.append(value)

with open(os.path.join(sys.path[0], 'data.csv'), 'a') as datafile:
    datafile.write(', '.join(values))
    datafile.write('\n')
