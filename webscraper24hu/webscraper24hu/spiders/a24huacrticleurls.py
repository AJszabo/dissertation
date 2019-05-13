# -*- coding: utf-8 -*-
import scrapy
from ..items import Webscraper24HuItem


class A24huacrticleurlsSpider(scrapy.Spider):
    name = '24huacrticleurls'
    allowed_domains = ['24.hu']
    start_urls = ["https://24.hu/tag/bevandorlas",
                "https://24.hu/tag/bevandorlo",
                "https://24.hu/tag/bevandorlok",
                "https://24.hu/tag/gazdasagi bevandorlok",
                "https://24.hu/tag/gazdasagi bevandorlo",
                "https://24.hu/tag/gazdasagi bevandorlas",
                "https://24.hu/tag/hatarserto",
                "https://24.hu/tag/illegalis bevandorlas",
                "https://24.hu/tag/illegalis bevandorlo",
                "https://24.hu/tag/illegalis bevandorlok",
                "https://24.hu/tag/menedekkero",
                "https://24.hu/tag/menekult",
                "https://24.hu/tag/menekultek",
                "https://24.hu/tag/menekultvalsag",
                "https://24.hu/tag/migracio",
                "https://24.hu/tag/migrans",
                "https://24.hu/tag/migransok"
                ]
    
    def parse(self, response):
        urls = response.css('.m-entryPost__link')
        times = response.css('.m-author__wrapCatDateTitulus')
        items = Webscraper24HuItem()
        i = 0
        for url in urls:
            time = times[i]
            date = time.css('::text').extract()
            url = url.xpath("@href").extract()
            i+=1
            items['date'] = date
            items['url'] = url

            yield items

        
        next_page = response.css('.next').xpath("@href").get()
        
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
        