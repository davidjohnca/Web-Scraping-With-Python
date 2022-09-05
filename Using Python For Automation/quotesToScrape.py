# 1. IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

# 2. CREATE URL PARSER
url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 3. ISOLATE ELEMENTS WANTED FOR EXTRACTION
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# 4. ITERATE THROUGH ELEMENTS TO EXTRACT THEM
for i in range(0, len(quotes)):
	print(quotes[i].text)
	print(authors[i].text)
	quote_tags = tags[i].find_all('a', class_='tag')
	for quote_tag in quote_tags:
		print(quote_tag.text)