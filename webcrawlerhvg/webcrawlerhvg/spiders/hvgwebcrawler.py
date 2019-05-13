import scrapy
from ..items import WebcrawlerhvgItem


class hvgwebcrawlerSpider(scrapy.Spider):
    name = 'hvgwebcrawler'
    allowed_domains = ['hvg.hu']
    start_urls = ["https://hvg.hu/cimke/bevandorlas",
                "https://hvg.hu/cimke/bevandorlo",
                "https://hvg.hu/cimke/bevandorlok",
                "https://hvg.hu/cimke/gazdasagi bevandorlok",
                "https://hvg.hu/cimke/gazdasagi bevandorlo",
                "https://hvg.hu/cimke/gazdasagi bevandorlas",
                "https://hvg.hu/cimke/hatarserto",
                "https://hvg.hu/cimke/illegalis bevandorlas",
                "https://hvg.hu/cimke/illegalis bevandorlo",
                "https://hvg.hu/cimke/illegalis bevandorlok",
                "https://hvg.hu/cimke/menedekkero",
                "https://hvg.hu/cimke/menekult",
                "https://hvg.hu/cimke/menekultek",
                "https://hvg.hu/cimke/menekultvalsag",
                "https://hvg.hu/cimke/migracio",
                "https://hvg.hu/cimke/migrans",
                "https://hvg.hu/cimke/migransok"]
    
    def parse(self, response):
        urls = response.css(".column-articlelist .heading-3 a")
        items = WebcrawlerhvgItem()
        for url in urls:
            url = url.xpath("@href").extract()
            url[0] = 'https://hvg.hu' + url[0]
            items['url'] = url

            yield items

        
        next_page = response.css('.next').xpath("@href").get()
        
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
        
