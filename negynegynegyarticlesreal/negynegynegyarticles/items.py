# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NegynegynegyarticlesItem(scrapy.Item):
    paragaph = scrapy.Field()
    tags = scrapy.Field()
    connections = scrapy.Field()
    start_url = scrapy.Field()
