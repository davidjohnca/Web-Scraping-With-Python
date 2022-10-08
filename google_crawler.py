from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)

query = str(input('Enter your query: '))
links = []

n_pages = 20
for page in range(1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    search = soup.find_all('div', class_="yuRUbf")
    for h in search:
        links.append(h.a.get('href'))
        print(h.a.get('href'))
        time.sleep(2)

df = pd.DataFrame(links)
df.to_csv('google_links.csv', index=False)

print('*' * 50)
print(f'Number of scraped items: {len(links)}')
print('Task complete!')
