# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from ..items import VshuarticlesItem

class VshuarticlesSpider(scrapy.Spider):
    name = 'vsponthuartives'
    allowed_domains = ['vs.hu']
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    urls=[]
    curr.execute("""SELECT DISTINCT * FROM 'vsUrl_tb'
                 ORDER BY url;
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
        items = VshuarticlesItem()
        text = ['']
        connections = ['']
        tags = ['']
        start_url = ['']
        p = response.css(".inner_margin li::text, .inner_margin p::text").extract()
        connection = response.css(".page_center .content a").xpath("@href").extract()
        tag = response.css(".tags .tag::text").extract()
        start_url[0] = response.request.url
        for paragaph in p:
            text[0] += " " + paragaph
        for c in connection:
            connections[0] += " " + c
        for t in tag:
            tags[0] += " " + t
        time = response.css(".date").extract()
        
        items['paragaph'] = text
        items['tags'] = tags
        items['connections'] = connections
        items['start_url'] = start_url
        items['time'] = time
        
        yield items
