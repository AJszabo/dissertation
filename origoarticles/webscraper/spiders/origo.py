# -*- coding: utf-8 -*-
import scrapy
from ..items import WebscraperItem
import sqlite3

class OrigoSpider(scrapy.Spider):
    name = "origo"
    allowed_domains = ["origo.hu"]
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    urls=[]
    curr.execute("""SELECT DISTINCT url FROM 'origoUrl_tb' WHERE 
                 url LIKE "%201801%" OR
                 url LIKE "%201802%" OR
                 url LIKE "%201803%" OR
                 url LIKE "%201804%" OR
                 url LIKE "%201805%" OR
                 url LIKE "%2017%" OR
                 url LIKE "%2016%" OR
                 url LIKE "%2015%" OR
                 url LIKE "%201405%" or
                 url LIKE "%201406%" or
                 url LIKE "%201407%" or
                 url LIKE "%201408%" or
                 url LIKE "%201409%" or
                 url LIKE "%201410%" or
                 url LIKE "%201411%" or
                 url LIKE "%201412%" ORDER BY url
                 """)
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urls.append(urlrow)
    start_urls = urls
    
    def parse(self, response):
        urls = response.css('#article-text')
        items = WebscraperItem()
        text = ['']
        connections = ['']
        time = ['']
        start_url = ['']
        for url in urls:
            tags = url.css("li::text,.p-kiemelt::text, p::text,cite::text,span::text").extract()
            connection = url.css("li a,.p-kiemelt a, p a,cite a").xpath("@href").extract()
            time = response.css("#article-date::text,.cikk-datum::text").extract()
            for paragaph in tags:
                text[0] += " " + paragaph
            for co in connection:
                connections[0] += " " + co
            response.request.url
            start_url[0] = response.request.url
            
            items['paragaph'] = text
            items['time'] = time
            items['connections'] = connections
            items['start_url'] = start_url
            yield items
        
        #next_page = response.css('.next a').xpath("@href").get()
        
        #if next_page is not None:
            #yield response.follow(next_page, callback= self.parse)
