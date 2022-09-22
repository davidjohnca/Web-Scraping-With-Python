from bs4 import BeautifulSoup
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


class GoogleSpider:
    def link_scraper():
        driver = webdriver.Chrome(
            '/Users/David/OneDrive - IFPI/Desktop/My Python Files/chromedriver', chrome_options=chrome_options)

        # Query to obtain links
        query = str(input('Enter your query: '))
        print('GoogleSpider has started crawling')
        print('Scraping all available links')

        # Initiate empty list to capture final results
        links = []

        # Specify number of pages on Google Search, each page contains 10 #links
        n_pages = 30
        for page in range(1, n_pages):
            url = "http://www.google.com/search?q=" + \
                query + "&start=" + str((page - 1) * 10)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # (OR)soup = BeautifulSoup(r.text, 'html.parser')

            search = soup.find_all('div', class_="yuRUbf")
            for item in search:
                links.append(item.a.get('href'))

        df = pd.DataFrame(links)
        df.to_csv('google_links.csv', index=False)

        print('Task complete! All scraped links are now saved in google_links.csv')


GoogleSpider.link_scraper()