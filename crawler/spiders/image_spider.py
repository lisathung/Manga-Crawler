import scrapy
import re 
from crawler.items import MangaPage

class image_spider(scrapy.Spider):

    name = "image_spider"
    #replace this url with the manga you want to download
    start_urls = ['https://mangakakalot.com/chapter/my918978/chapter_1']
    
    def parse(self,response):
        #basic parse method
        url = response.css('head link::attr(href)').extract_first()
        yield scrapy.Request(url,self.parse_chapters)

    def parse_chapters(self , response):
        #set a cap on the max number of chapters you want to download
        max_chapter = 2
        
        #grab the image urls and yield a request to handle them
        for item in response.css('div.vung-doc img::attr(src)').extract():
            yield scrapy.Request(item, self.parse_pages)
        
        #Extract link to next chapter and visit it
        for a in response.css('div.option_wrap a'):
            link = a.css('a::attr(href)').extract_first()
            current_chapter = int(re.search('(chapter_)[0-9]+' , link).group(0)[8:])

            #check max chapter
            if current_chapter <= max_chapter:
                yield response.follow(a , callback=self.parse_chapters)
            else:
                pass
        
    def parse_pages(self,response):
        # grab the URL of the image
        url = response.request.url 
        
        #grab only the relevant bits, leave out the '/' and .jpg 
        chapter = re.search("(/chapter_)[0-9]+", url).group(0)[1:]
        page = re.search("[0-9]+(.jpg)", url).group(0)[:-4]

        #yield the result
        yield MangaPage(image_urls=[url] , manga_chapter=chapter , manga_page=page)