# status code checker
import requests
import csv
import time

SLEEP = 0 # Time in seconds the script should wait between requests
url_list = []
url_statuscodes = []
url_statuscodes.append(["url","status_code"]) # set the file header for output


def getStatuscode(url):
    try:
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)

    except:
        return -1


# Url checks from file Input
# use one url per line that should be checked
with open('audiusReportedLinksUMG(2022-08-01 to present).csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        url_list.append(row[0])


# Loop over full list
for url in url_list:
    print(url)
    check = [url,getStatuscode(url)]
    time.sleep(SLEEP)
    url_statuscodes.append(check)

# Save file
with open("urls_withStatusCode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(url_statuscodes)