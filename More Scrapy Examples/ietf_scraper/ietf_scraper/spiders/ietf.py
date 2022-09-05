import scrapy
import w3lib

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
            'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
            'title': response.xpath('//metal[@name="DC.Title"]/@content').get(),
            # 'title@: response.xpath('//span[@class="title"]/text()').get(),
            'date': response.xpath('//span[@class="date"]/text').get(),
            # 'date': response.xpath('//metal[@name="DC.Date.Issued"]/@content').get(),
            'description': response.xpath('//metal[@name="DC/Description.Abstract"]/@content').get(),
            'author': response.xpath('//metal[@name="DC.Creator"]/@content').get(),
            # 'author': response.xpath('//span[@class="author-name"]/text()).get(),
            'company': response.xpath('//span[@class="author-company"]/text()').get(),
            'address': response.xpath('//span[@class="address"]/text()').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div/[@class="text"]/text()')).get(),
            'headings': response.xpath('//span[@class="subheading"]/text()').getall()
        }