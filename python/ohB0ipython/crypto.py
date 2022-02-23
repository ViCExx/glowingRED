import requests
import pprint
import csv
from datetime import datetime

def get_price(symbol):
  url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
  parameters = {
    'symbol': symbol,
    'convert': 'USD'
  }
  
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '6292efb6-82b6-4806-80c1-e54a9a4044ed'
  }
  response = requests.get(url, params=parameters, headers=headers)

  return response.json().get('data').get(symbol)[0]['quote']['USD']['price']

#Tickers = ['BTC', 'ETH']
Tickers = ['BTC', 'ETH', 'DOT', 'XRP', 'DOGE','SHIB', 'ADA', 'SOL']

with open('CRYPTO.csv', 'a+', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["SYMBOL","USD PRICE", "DATEnTIME"])
  for ticker in Tickers:
    writer.writerow([ticker, get_price(ticker),datetime.now()])
    print(ticker, "is: ")
    print(get_price(ticker))
    next(iter(ticker))

  # was very excited to get this working with a list in a for loop.
  # next project will be to create an input and have it deliver the stats
