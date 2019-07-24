import scrapy
import re 
from crawler.items import MangaPage
import logging

# initialize the log settings
logging.basicConfig(filename='app.log',level=logging.INFO)
filePointer = open('appFile','w')

class image_spider(scrapy.Spider):
    '''
    the value of the 'start_urls' variable will be passed as a parameter in the main.py file 
    '''
    name = "image_spider"
    
    #overwriting the constructor to include custom arguments
    def __init__(self,my_url='',max_chapter_no=0,*args,**kwargs):
        super(image_spider, self).__init__(*args, **kwargs)
        self.start_urls = [my_url]
        self.max_chapters = int(max_chapter_no)

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
            link = a.css('a::attr(href)').extract_first()
            current_chapter = int(re.search('(chapter_)[0-9]+' , link).group(0)[8:])

            #set a cap on the max number of chapters you want to download
            if current_chapter <= self.max_chapters:
                yield response.follow(a , callback=self.parse_chapters)
            else:
                pass
        
    def parse_pages(self,response):
        # grab the URL of the image
        url = response.request.url 

        logging.debug('URL:{}'.format(url))
        #grab only the relevant bits, leave out the '/' and .jpg 
        chapter = re.search("[\/][\w]+(chapter)[\w]+[\/]", url).group(0).replace('/','')
        page = re.search("[0-9]+(.jpg)", url).group(0)[:-4]
   
        #yield the result
        yield MangaPage(image_urls=[url] , manga_chapter=chapter , manga_page=page)


filePointer.close()
