import os
import alpaca_trade_api as alpaca
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

"""
Get connected
=============
"""
API_KEY = os.environ.get('ALP_TOKEN')
API_SECRET = os.environ.get('ALP_KEY')

api = alpaca.REST(API_KEY, API_SECRET, 'https://paper-api.alpaca.markets')

"""
Show graph
==========
"""

df = api.get_barset('YNDX', 'day', limit=42).df['YNDX']

df.rename(columns={'open': 'Open',
                   'high': 'High',
                   'low': 'Low',
                   'close': 'Close',
                   'volume': 'Volume'},
          inplace=True)

#plot
mpf.plot(df, type='candle',
         title='YNDX - 42 days',
         ylabel='PRICE (USD)',
         style='nightclouds')

