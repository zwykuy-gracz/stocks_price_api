import requests
from datetime import datetime as dt


NEWS_URL = 'https://newsapi.org/v2/everything'
NEWS_API = '6bbfd8d95989467db4710f483f3b03a7'
STOCK = "TSLA"
new_titles = []

parameters = {
    'q': STOCK,
    'from': dt.date(dt.now()),
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API,
}

response = requests.get(url=NEWS_URL, params=parameters)
response.raise_for_status()

news_data = response.json()
three_newest = news_data['articles'][:3]
for news in three_newest:
    news_title = news['title']
    new_titles.append(news_title)