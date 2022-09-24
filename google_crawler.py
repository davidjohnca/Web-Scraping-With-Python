from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--headless')


class GoogleSpider:
    def link_scraper():
        url = 'https://www.google.com/'
        driver = webdriver.Chrome(
            '/Users/davidaceres/Desktop/my_python_files/chromedriver', options=chrome_options)
        driver.get(url)

        driver.implicitly_wait(2)

        cookies = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
        cookies.click()

        driver.implicitly_wait(2)

        search = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.send_keys('python courses london')
        search.submit()

        driver.implicitly_wait(2)

        query = str(input('Enter your query: '))
        print('GoogleSpider has started crawling')
        print('Scraping all available links')

        links = []

        pages = 20

        for page in range(1, pages):
            url = url = "http://www.google.com/search?q=" + \
                query + "&start=" + str((page - 1) * 10)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            search = soup.find_all('div', class_="yuRUbf")

            for item in search:
                print(item.a.get('href'))

                link_item = {
                    'links': item.a.get('href')
                }

                links.append(link_item)

        df = pd.DataFrame(links)

        print(df)
        print('Task complete!')


GoogleSpider.link_scraper()
