# -*- coding: utf-8 -*-
import scrapy
from ..items import NegynegynegyarticlesItem


class A24huacrticleurlsSpider(scrapy.Spider):
    name = 'negynegynegyarticles'
    allowed_domains = ['444.hu']
    start_urls = ["https://444.hu/tag/bevandorlas",
                "https://444.hu/tag/bevandorlo",
                "https://444.hu/tag/bevandorlok",
                "https://444.hu/tag/gazdasagi bevandorlok",
                "https://444.hu/tag/gazdasagi bevandorlo",
                "https://444.hu/tag/gazdasagi bevandorlas",
                "https://444.hu/tag/hatarserto",
                "https://444.hu/tag/illegalis bevandorlas",
                "https://444.hu/tag/illegalis bevandorlo",
                "https://444.hu/tag/illegalis bevandorlok",
                "https://444.hu/tag/menedekkero",
                "https://444.hu/tag/menekult",
                "https://444.hu/tag/menekultek",
                "https://444.hu/tag/menekultvalsag",
                "https://444.hu/tag/migracio",
                "https://444.hu/tag/migrans",
                "https://444.hu/tag/migransok"]
    
    def parse(self, response):
        urls = response.css('h3 a')
        items = NegynegynegyarticlesItem()
        for url in urls:
            url = url.xpath("@href").extract()
            items['url'] = url

            yield items

        
        next_page = response.css('.infinity-next').xpath("@href").get()
        
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
        