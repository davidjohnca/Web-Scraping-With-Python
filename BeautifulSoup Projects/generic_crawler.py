import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

quotes_list = []

for x in range(1, 11):
  url = f'http://quotes.toscrape.com/page/{x}/'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  quotes = soup.find_all('div', class_='quote')

  for quote in quotes:
    text = quote.find('span', {'class': 'text'})
    author = quote.find('small', {'class': 'author'})
    quote_elements = {
      'Text': text.text.replace('\n', '').replace('\t', '').strip(),
      'Author': author.text.replace('\n', '').replace('\t', '').strip(),
    }
    quotes_list.append(quote_elements)
    print(quote_elements)
    time.sleep(2)

df = pd.DataFrame(quotes_list)
df.to_csv('quotes.csv', index=False)

print('*' * 50)
print(f'Number of scraped items: {len(quotes_list)}')
print('Task complete!')
