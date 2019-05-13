# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Webscraper24HuItem(scrapy.Item):
    paragaph = scrapy.Field()
    time = scrapy.Field()
    connections = scrapy.Field()
    start_url = scrapy.Field()
