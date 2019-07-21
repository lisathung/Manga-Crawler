import scrapy

class quote_spider(scrapy.Spider):
    name = "quote_spider"

    start_urls = ['http://quotes.toscrape.com/page/1/']
    
    def parse(self , response):
        for item in response.css('div.quote'):
            yield{
                'text' : item.css('span.text::text').get(),
                'author' : item.css('small.author::text').get(),
                'tags' : item.css('iv.tags a.tag::text').get()
            }
        