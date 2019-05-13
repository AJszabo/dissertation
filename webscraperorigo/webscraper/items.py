# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscraperItem(scrapy.Item):
    # define the fields for your item here like:
    tags = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    
    