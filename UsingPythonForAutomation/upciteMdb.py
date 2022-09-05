# IMPORT NECESSARY LIBRARIES
import requests
import json

# CREATE URL GETTER
base_url = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'073366118238'}
response = requests.get(base_url, params=parameters)
#print(response.url)

# CREATE JSON LOADS VARIABLE
content = response.content
info = json.loads(content)
#print(type(info))
#print(info)

# ISOLATE AND EXTRACT DESIRED ELEMENTS
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)