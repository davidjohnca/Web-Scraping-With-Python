# IMPORT THE NECESSART LIBRARIES
from bs4 import BeautifulSoup
import requests

# CREATE URL PARSER
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# ISOLATE ITEMS WANTED FOR EXTRACTION
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

# CREATE PAGINATION
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
	pageNum = int(link.text) if link.text.isdigit() else None
	if pageNum != None:
		x = link.get('href')
		urls.append(x)

print(urls)

count = 1

# EXTRACT ELEMENTS FROM EVERY PAGE
for i in urls:
	newUrl = url + i
	response = requests.get(newUrl)	
	for i in items:
		itemName = i.find('h4', class_='card-title').text.strip('\n')
		itemPrice = i.find('h5').text
		print(f'{count}) Item Name: {itemName}, Price: {itemPrice}')
		print()
		count += 1