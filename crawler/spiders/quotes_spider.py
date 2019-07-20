import scrapy

class quote_spider(scrapy.Spider):
    name = "quote_spider"

    start_urls = ['http://quotes.toscrape.com/page/1/']
    
    def parse(self , response):
        page = response.url.split("/")[-2]
        filename = "quotes-%s.html"%page
        with open (filename, 'wb') as f:
            f.write(response.body)
        