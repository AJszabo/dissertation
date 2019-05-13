# -*- coding: utf-8 -*-
import scrapy
from ..items import WebscraperItem


class OrigoSpider(scrapy.Spider):
    name = "origo"
    allowed_domains = ["origo.hu"]
    start_urls = ["https://cimkezes.origo.hu/cimkek/migrans/index.html?tag=migr%E1ns&hits=100000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/hatarserto/index.html?tag=hat%E1rs%E9rt%F5&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/menekult/index.html?tag=menek%FClt&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/illegalis-bevandorlo/index.html?tag=illeg%E1lis%20bev%E1ndorl%F3&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/migracio/index.html?tag=migr%E1ci%F3&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/illegalis-bevandorlas/index.html?tag=illeg%E1lis%20bev%E1ndorl%E1s&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/menekulttabor/index.html?tag=menek%FCltt%E1bor&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/bevandorlo/index.html?tag=bev%E1ndorl%F3&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/migransok/index.html?tag=migr%E1nsok&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/gazdasagi-bevandorlok/index.html?tag=gazdas%E1gi%20bev%E1ndorl%F3k&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/illegalis-bevandorlok/index.html?tag=illeg%E1lis%20bev%E1ndorl%F3k&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/menekultvalsag/index.html?tag=menek%FCltv%E1ls%E1g&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/roszke/index.html?tag=R%F6szke&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/bevandorlok/index.html?tag=bev%E1ndorl%F3k&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/kvota/index.html?tag=kv%F3ta&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/kerites/index.html?tag=ker%EDt%E9s&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/menedekkero/index.html?tag=mened%E9kk%E9r%F5&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/hatarzar/index.html?tag=hat%E1rz%E1r&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/bevandorlas/index.html?tag=bev%E1ndorl%E1s&hits=10000&offset=10",
                   "https://cimkezes.origo.hu/cimkek/menekultek/index.html?tag=menek%FCltek&hits=10000&offset=10"]
    
    def parse(self, response):
        urls = response.css('#wrap-main .news-item')
        items = WebscraperItem()

        for url in urls:
            tags = url.css(".clearfix a::text").extract()
            date = url.css('.pubdate::text').extract()
            title = url.css(".news-title::text").extract()
            url = url.css(".news-title").xpath("@href").extract()
            
            items['tags'] = tags
            items['date'] = date
            items['title'] = title
            items['url'] = url

            yield items

        
        #next_page = response.css('.next a').xpath("@href").get()
        
        #if next_page is not None:
            #yield response.follow(next_page, callback= self.parse)