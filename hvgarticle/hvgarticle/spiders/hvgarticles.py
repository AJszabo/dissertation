# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from ..items import HvgarticleItem

class HvgarticlesSpider(scrapy.Spider):
    name = 'hvgarticles'
    allowed_domains = ['hvg.com']
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    urls=[]
    curr.execute("""SELECT url FROM 'hvgUrl_tb' WHERE
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
                 url LIKE "%201412%" ORDER BY url;
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
        items = HvgarticleItem()
        text = ['']
        connections = ['']
        tags = ['']
        start_url = ['']
        p = response.css(".entry-summary p::text,.entry-summary  p a::text, .entry-summary p a em::text,.entry-content p::text,.entry-content p a::text, .entry-content p a em::text").extract()
        connection = response.css(".entry-summary p a, .entry-summary p a em,.entry-content p,.entry-content p a, .entry-content p a em").xpath("@href").extract()
        tag = response.css(".article-tags .tag::text").extract()
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