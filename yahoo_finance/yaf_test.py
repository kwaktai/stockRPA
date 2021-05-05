# import pandas_datareader as pdr
# import pandas as pd
# df = pdr.get_data_yahoo('TSLA')
# print(df)


import yfinance as yf
import time

msft = yf.Ticker("MSFT")
print(msft.history(period="max"))
