# -*- coding: utf-8 -*-
import scrapy
from ..items import WebscraperItem


class OrigoSpider(scrapy.Spider):
    name = "origo"
    allowed_domains = ["origo.hu"]
    start_urls = ["https://cimkezes.origo.hu/cimkek/migracio/index.html?tag=migr%E1ci%F3&hits=10000&offset=10",
                  "https://cimkezes.origo.hu/cimkek/menekult/index.html?tag=menek%FClt&offset=0&hits=10000",
                  "https://cimkezes.origo.hu/cimkek/bevandorlas/index.html?tag=bev%E1ndorl%E1s&offset=0&hits=10000",
                  "https://cimkezes.origo.hu/cimkek/illegalis-bevandorlas/index.html?tag=illeg%E1lis+bev%E1ndorl%E1s&offset=0&hits=10000",
                  "https://cimkezes.origo.hu/cimkek/kvota/index.html?tag=kv%F3ta&offset=0&hits=10000",
                  "https://cimkezes.origo.hu/cimkek/menedekkero/index.html?tag=mened%E9kk%E9r%F5&offset=0&hits=10000",
                  "https://cimkezes.origo.hu/cimkek/menekultek/index.html?tag=menek%FCltek&offset=0&hits=10000",
                  "https://cimkezes.origo.hu/cimkek/menekult/index.html?tag=menek%FClt&offset=0&hits=10000"]
    
    def parse(self, response):
        urls = response.css('#wrap-main .clearfix a')
        items = WebscraperItem()
        myCountlist =[]
        for url in urls:
            tags = url.css("::text").extract()
         
            items['tags'] = tags
            yield items
        print(myCountlist)
        
        #next_page = response.css('.next a').xpath("@href").get()
        
        #if next_page is not None:
            #yield response.follow(next_page, callback= self.parse)