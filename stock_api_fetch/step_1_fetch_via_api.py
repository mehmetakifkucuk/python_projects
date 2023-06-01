# import necessary libraries
import pandas as pd
# import numpy as np
import requests

# define API key and base URL
api_key = '02KCC7JFN4DFFWMH'
base_url = 'https://www.alphavantage.co/query?function='

# define function to request stock data
def get_stock_data(symbol, interval):
  url = base_url + 'TIME_SERIES_' + interval + '_ADJUSTED&symbol=' + symbol + '&apikey=' + api_key
  response = requests.get(url)
  data = response.json()
  df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
  df.index = pd.to_datetime(df.index)
  df.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted Close', 'Volume', 'Dividend', 'Split Coefficient']
  df = df.astype(float)
  return df

# fetch stock data for a sample symbol and interval
symbol = 'AAPL'
interval = 'DAILY'
data = get_stock_data(symbol, interval)

# calculate daily returns
data['Return'] = (data['Close'] / data['Close'].shift(1)) - 1

# calculate 50-day moving average
data['MA50'] = data['Close'].rolling(window=50).mean()

# print the data
print(data.head())