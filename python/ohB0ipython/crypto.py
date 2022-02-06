import requests
import pprint

def get_price(symbol):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
    'symbol': symbol
  }
  
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '<get from coinmarket>'
  }
  response = requests.get(url, params=parameters, headers=headers)

  #return response.json().get('data').get(symbol).get('quote').get('USD').get('price')
  return response.json().get('data', {}).get(symbol,{}).get('quote',{}).get('USD',{'price','percent_change_1h'})
Tickers = ['BTC', 'ETH']
#Tickers = ['BTC', 'ETH', 'DOT', 'XRP', 'DOGE','SHIB', 'ADA', 'SOL']
for ticker in Tickers:
  next(iter(ticker))
  print(ticker, "is: ")
  pprint.pprint(get_price(ticker))

  # was very excited to get this working with a list in a for loop.
  # next project will be to create an input and have it deliver the stats
  