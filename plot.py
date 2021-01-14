#!/usr/bin/python3
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv', parse_dates=[0])
for series in ('patrons', 'monthly', 'total'):
    px.line(df, x='date', y=[f'ns_{series}', f'357_{series}']).show()
