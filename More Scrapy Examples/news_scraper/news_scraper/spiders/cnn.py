import scrapy
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle

def generate_start_urls():
    years = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
    months = ['1','2','3','4','5','6','7','8','9','10','11','12']
    return ['https://www.cnn.com/sitemaps/articles-{}-{}.xml'.format(year, month) for year in years for month in months]

class CnnSpider(SitemapSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    sitemap_urls = ['https://edition.cnn.com/sitemaps/article-2022-08.xml']

    def parse_item(self, response):
        return {'url':response.url, 'count':response.text.count('<url>')}