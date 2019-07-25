# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MangaPage(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    image_urls = scrapy.Field()
    manga_chapter = scrapy.Field()
    manga_page = scrapy.Field()
