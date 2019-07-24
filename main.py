'''
Main file. Does the following:

1. accept custom parameters
2. create new spider process, pass custom parameters and run 
'''

from scrapy.crawler import CrawlerProcess
from crawler.spiders.image_spider import image_spider

start_url = input("Enter start url of the format https://mangakakalot.com/chapter/my918978/chapter_1\n")
max_chapters = int(input('Enter the maximum numeber of chapters you want to download. Cannot be less than 1\n'))
#start_url = 'https://mangakakalot.com/chapter/gotoubun_no_hanayome/chapter_0.1'

process = CrawlerProcess()
process.crawl(image_spider, my_url=start_url, max_chapter_no=max_chapters )
process.start()