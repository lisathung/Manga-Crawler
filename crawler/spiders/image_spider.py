import scrapy
import re 
from crawler.items import MangaPage
import logging
import time

# initialize the log settings
logging.basicConfig(filename='app.log',level=logging.INFO)
filePointer = open('appFile','w')

class image_spider(scrapy.Spider):
    '''
    the value of the 'start_urls' variable will be passed as a parameter in the main.py file 
    '''
    name = "image_spider"
    # only for https://www.readm.org/
    base_url = 'https://www.readm.org/'

    #overwriting the constructor to include custom arguments
    def __init__(self,my_url='',max_chapter_no=0,*args,**kwargs):
        super(image_spider, self).__init__(*args, **kwargs)
        self.start_urls = [my_url]
        self.max_chapters = int(max_chapter_no)
        self.chapter_counter = 0

    def parse(self,response):
        #basic parse method for the first link
        # url = response.css("head meta[property='og:url']::attr(content)").extract_first()

        logging.debug('requestURL:{}'.format(self.start_urls[0]))
        yield scrapy.Request(self.start_urls[0],self.parse_chapters)

    def parse_chapters(self, response):
        # #grab the image urls and yield a request to handle them(DOMEKANO)
        # for item in response.css('div.vung-doc img::attr(src)').extract():
        #     yield scrapy.Request(item, self.parse_pages)
        
        #grab the image urls and yield a request to handle them
        # for item in response.css('div.container-chapter-reader img::attr(src)').extract():
        #     yield scrapy.Request(item, self.parse_pages)
        for item in response.css('div.ch-images.ch-image-container ::attr(src)').extract():
            logging.debug('LINK TYPE:{}'.format(type(item)))
            logging.debug('IMG LINK:{}'.format(self.base_url+item))
            yield scrapy.Request(self.base_url+item, self.parse_pages)
        
        # #Extract link to next chapter and visit it (DOMEKANO)
        # for a in response.css('div.option_wrap a'):
            # link = a.css('a::attr(href)').extract_first()
            # current_chapter = int(re.search('(chapter_)[0-9]+' , link).group(0)[8:])
            
            # #set a cap on the number of chapters you want to download
            # if current_chapter <= self.max_chapters:
            #     yield response.follow(link, callback=self.parse_chapters)
            # else:
            #     pass
        
        #Extract link to next chapter and visit it (ATOWNWHEREYOULIVE)
        link = response.css('a.item.navigate.ch-next-page.navigate-next ::attr(href)').extract()[-1]
        logging.debug('LINK:{}'.format(link))

        # current_chapter = int(re.search('[0-9]+\/(all-pages)' , link).group(0)[8:])    
        self.chapter_counter += 1

        #There is a cap on the number of chapters you want to download
        if self.chapter_counter <= self.max_chapters:
            yield response.follow(link, callback=self.parse_chapters)
        else:
            pass
    
    def parse_pages(self,response):
        # grab the URL of the image
        url = response.request.url 

        # logging.debug('URL:{}'.format(url))
        #grab only the relevant bits, leave out the '/' and .jpg 
        # chapter = re.search("[\/][\w]*(chapter)[\w]+[\/]", url).group(0).replace('/','')
        # page = re.search("[0-9]+(.jpg)", url).group(0)[:-4]
        
        #extract the relevant portion "/chapter_num/page_number" and split
        logging.debug('LINK FOR PARSING:{}'.format(url))
        filename = re.search('[0-9]+(\/p\_)[0-9]+\.(gif|jpe?g|tiff?|png|webp|bmp)',url).group(0).split('/')
        chapter = 'chapter_' + filename[0]
        page = filename[1]

        logging.debug('DATA:{}{}{}'.format([url],chapter,page))
        #yield the result
        yield MangaPage(image_urls=[url] , manga_chapter=chapter , manga_page=page)

filePointer.close()