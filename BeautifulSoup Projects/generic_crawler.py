from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
import time

results_list = []

for x in range(1,11): 
  print(f'Page {x} is being scraped')

url = f'http://www.example.com/page{x}'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

all_info = soup.find_all('exampleTag', class_='exampleValue')

for item in all_info:
  time.sleep(2)
  exampleElement = item.find('exampleTag', class_='exampleValue')
  elements = {
    'exampleKey':exampleElement,
  }
  results_list.append(elements)

df = pd.DataFrame(results_list)
df.to_csv('example.xlsx', index=False)

print('*' * 50)
print('Task complete!')
