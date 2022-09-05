import scrapy
import time
from scrapy_selenium import SeleniumRequest

def wait(driver):
    time.sleep(1)
    return True

class DunkinSpider(scrapy.Spider):
    name = 'dunkin'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://www.krispykreme.co.uk/find-store?store-search=Piccadilly+Circus%2C+London%2C+UK&store-search-type=']

    def make_resquests_from_url(self, url):
        return SeleniumRequest(url=url, wait_time=10, wait_until=wait)

    def parse(self, response):
        return {'addresses':response.xpath('//address[@class="storefinder-item__address"]/text()').getall()}