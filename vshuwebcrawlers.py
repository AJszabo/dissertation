# -*- coding: utf-8 -*-
import scrapy


class VshuwebcrawlersSpider(scrapy.Spider):
    name = 'vshuwebcrawlers'
    allowed_domains = ['vs.hu']
    start_urls = ['http://vs.hu/']

    def parse(self, response):
        pass
