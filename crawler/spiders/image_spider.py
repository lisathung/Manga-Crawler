import scrapy
from crawler.items import MangaPage

class image_spider(scrapy.Spider):

    name = "image_spider"
    start_urls = ['https://mangakakalot.com/chapter/my918978/chapter_1']

    def parse(self,response):
        #basic parse method
        url = response.css('head link::attr(href)').extract_first()
        yield scrapy.Request(url,self.parse_chapters)

    def parse_chapters(self , response):
        #grab the image urls and yield a request to handle them
        for item in response.css('div.vung-doc img::attr(src)').extract():
            yield scrapy.Request(item, self.parse_pages)
        
        #Extract link to next chapter and visit it
        for a in response.css('div.option_wrap a'):
            yield response.follow(a , callback=self.parse_chapters)

    def parse_pages(self,response):
        # grab the URL of the image
        url = response.request.url
        #yield the result
        yield MangaPage(image_urls=[url])
    
    #files names and folders