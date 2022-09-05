from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl.workbook import Workbook

results_list = []

# set the starting page and the page after the last one, which isn't included
for x in range(1,11):
    print(f'Page {x} has been scraped')
# paste the url with "x" as the page number
    url = f'http://www.example.com/page{x}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
# define the element from where the information will be extracted
    all_info = soup.find_all('exampleTag', class_='exampleValue')

    for i in all_info:
# define the element of the information you wisth to extract
# if you want a specific attribute, indicate it inside "['']" after the parentheses (for example, "soup.find_all('a')['href']")
# if you want the text inside a tag, simply put ".text" after the parentheses (for example, "soup.find_all('h2').text")
# notice that ".find_all" gets all elements, and ".find" only gets the first one
        exampleElement = i.find('exampleTag', class_='exampleValue')
# store the information inside a dictionary
        elements = {
            'exampleKey':exampleElement,
        }
        results_list.append(elements)

df = pd.DataFrame(results_list)
# define the name of the excel file
df.to_excel('example.xlsx', index=False)

print('Task complete!')
