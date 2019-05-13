# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VshuarticlesItem(scrapy.Item):
    # define the fields for your item here like:
    paragaph = scrapy.Field()
    tags = scrapy.Field()
    connections = scrapy.Field()
    start_url = scrapy.Field()
    time = scrapy.Field()