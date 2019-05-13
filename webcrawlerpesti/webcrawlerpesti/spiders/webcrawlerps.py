# -*- coding: utf-8 -*-
import scrapy
from ..items import WebcrawlerpsItem
class WebcrawlerpsSpider(scrapy.Spider):
    name = 'webcrawlerps'
    allowed_domains = ['pestisracok.hu']
    start_urls = ["https://pestisracok.hu/tag/bevandorlas",
                "https://pestisracok.hu/tag/bevandorlo",
                "https://pestisracok.hu/tag/bevandorlok",
                "https://pestisracok.hu/tag/gazdasagi bevandorlok",
                "https://pestisracok.hu/tag/gazdasagi bevandorlo",
                "https://pestisracok.hu/tag/gazdasagi bevandorlas",
                "https://pestisracok.hu/tag/hatarserto",
                "https://pestisracok.hu/tag/illegalis bevandorlas",
                "https://pestisracok.hu/tag/illegalis bevandorlo",
                "https://pestisracok.hu/tag/illegalis bevandorlok",
                "https://pestisracok.hu/tag/menedekkero",
                "https://pestisracok.hu/tag/menekult",
                "https://pestisracok.hu/tag/menekultek",
                "https://pestisracok.hu/tag/menekultvalsag",
                "https://pestisracok.hu/tag/migracio",
                "https://pestisracok.hu/tag/migrans",
                "https://pestisracok.hu/tag/migransok"]
    
    def parse(self, response):
        urls = response.css(".infinite-post")
        items = WebcrawlerpsItem()
        for i in urls:
            url = i.css(".widget-full-list-text a").xpath("@href").extract()
            time = i.css(".widget-post-date::text").extract()
            items['url'] = url
            items['time'] = time
            

            yield items

        
        next_page = response.css('.current+ .inactive').xpath("@href").get()
        
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)