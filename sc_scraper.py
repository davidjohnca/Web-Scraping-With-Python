import scrapy

class MySpider(scrapy.Spider):
    name = 'crawler'
    
# specify the allowed domain(s)
    allowed_domains = ['example.com']
    
# specify the start url(s)
    start_urls = ['http://www.example.com/']

    def parse(self, response):
        
# define the element from where the information will be extracted
        for i in response.css('exampleTag.exampleClassValue'):
        
''' define the element of the information you want to extract and store it inside a dictionary
if you want a specific attribute, indicate it by putting "::attr(exampleAttribute)" after the 
class value. If you want the text inside a tag, simply put "::text" after the class value '''
            yield {
                'exampleKey':response.css('exampleTag.exampleClassValue').get()
            }
        
# define the pagination element
        next_page = response.css('exampleTag.exampleClassValue::attr(href)')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

''' to create a csv file, excel, json, etc., simply type in the terminal 
"scrapy crawl exampleSpider -o exampleFile.exampleFormat -t exampleFormat" '''
