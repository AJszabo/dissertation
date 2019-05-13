# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from ..items import IndexarticlesItem

class IndexarticleSpider(scrapy.Spider):
    name = 'indexarticle'
    allowed_domains = ['index.hu']
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    urls=[]
    curr.execute("""SELECT DISTINCT * FROM 'indexUrl_tb' WHERE
                 url LIKE "%2018/01%" OR
                 url LIKE "%2018/02%" OR
                 url LIKE "%2018/03%" OR
                 url LIKE "%2018/04%" OR
                 url LIKE "%2018/05%" OR
                 url LIKE "%2017%" OR
                 url LIKE "%2016%" OR
                 url LIKE "%2015%" OR
                 url LIKE "%2014/05%" or
                 url LIKE "%2014/06%" or
                 url LIKE "%2014/07%" or
                 url LIKE "%2014/08%" or
                 url LIKE "%2014/09%" or
                 url LIKE "%2014/10%" or
                 url LIKE "%2014/11%" or
                 url LIKE "%2014/12%" ORDER BY url""")
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urls.append(urlrow)
    start_urls = urls
    
    def parse(self, response):
        items = IndexarticlesItem()
        text = ['']
        connections = ['']
        tags = ['']
        start_url = ['']
        p = response.css(".cikk-torzs li::text , .cikk-torzs p ::text, .lead::text").extract()
        connection = response.css("p a").xpath("@href").extract()
        tag = response.css(".cikk-cimkek .cimke::text").extract()
        start_url[0] = response.request.url
        for paragaph in p:
            text[0] += " " + paragaph
        for c in connection:
            connections[0] += " " + c
        for t in tag:
            tags[0] += " " + t
               
        
        items['paragaph'] = text
        items['tags'] = tags
        items['connections'] = connections
        items['start_url'] = start_url
        
        yield items
