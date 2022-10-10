import requests

APLHAVANTAGE_URL = 'https://www.alphavantage.co/query'
APLHAVANTAGE_API = 'HFQ0KTZ3RAJR42VY'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alphavantage_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': APLHAVANTAGE_API,
}


response = requests.get(url=APLHAVANTAGE_URL, params=alphavantage_parameters)
response.raise_for_status()

yesterdays_value = list(response.json()["Time Series (Daily)"].values())[0]
yesterdays_close = yesterdays_value['4. close']