'''
Main file. Does the following:

1. accept custom arguments
2. create new spider process, pass custom arguments and run 
'''

from scrapy.crawler import CrawlerProcess
from crawler.spiders.image_spider import image_spider
from scrapy.utils.project import get_project_settings

start_url = str(input("Enter start url of the format https://mangakakalot.com/chapter/my918978/chapter_1\n"))
max_chapters = int(input('Enter the maximum numeber of chapters you want to download. Cannot be less than 1\n'))

process = CrawlerProcess(get_project_settings())
process.crawl(image_spider, my_url=start_url, max_chapter_no=max_chapters )
process.start()
