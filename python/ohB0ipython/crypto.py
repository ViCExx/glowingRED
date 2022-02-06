import requests
import pprint

def get_price(symbol):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
    'symbol': symbol
  }

  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '6292efb6-82b6-4806-80c1-e54aa4044ed' #missing the 9
  }
  response = requests.get(url, params=parameters, headers=headers)

  return response.json().get('data', {}).get(symbol, {}).get('quote', {}).get('USD', {}).get('price',{})
  #return response.json().get('data', {})

pprint.pprint(get_price('ETH'))