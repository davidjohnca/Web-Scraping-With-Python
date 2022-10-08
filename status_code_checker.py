import requests
import csv
import time

SLEEP = 0
url_list = []
url_statuscodes = []
url_statuscodes.append(["url","status_code"])

def getStatuscode(url):
    try:
        r = requests.head(url,verify=False,timeout=5)
        return (r.status_code)
    except:
        return -1

with open('urls.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        url_list.append(row[0])

for url in url_list:
    print(url)
    check = [url,getStatuscode(url)]
    time.sleep(SLEEP)
    url_statuscodes.append(check)

with open("urls_withStatusCode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(url_statuscodes)
