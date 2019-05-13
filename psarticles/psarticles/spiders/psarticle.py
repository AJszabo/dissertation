    # -*- coding: utf-8 -*-
import scrapy
import sqlite3
from ..items import PsarticlesItem


class PsarticleSpider(scrapy.Spider):
    name = 'psarticle'
    allowed_domains = ['pestisracok.hu']
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    urls=[]
    curr.execute("""SELECT url FROM 'psUrl_tb' WHERE
                 time LIKE "%2018-01%" OR
                 time LIKE "%2018-02%" OR
                 time LIKE "%2018-03%" OR
                 time LIKE "%2018-04%" OR
                 time LIKE "%2018-05%" OR
                 time LIKE "%2017%" OR
                 time LIKE "%2016%" OR
                 time LIKE "%2015%" OR
                 time LIKE "%2014-05%" OR
                 time LIKE "%2014-06%" OR
                 time LIKE "%2014-07%" OR
                 time LIKE "%2014-08%" OR
                 time LIKE "%2014-09%" OR
                 time LIKE "%2014-10%" OR
                 time LIKE "%2014-11%" OR
                 time LIKE "%2014-12%" ORDER BY url
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
        items = PsarticlesItem()
        text = ['']
        connections = ['']
        tags = ['']
        start_url = ['']
        time = ['']
        p = response.css("#content-area p::text , strong::text").extract()
        connection = response.css("#content-area a").xpath("@href").extract()
        tag = response.xpath(".//*[@id='left-content']/div[4]/span[2]/a[1]").css("::text").extract()
        time = response.xpath("//*[@id='left-content']/div[2]/span/time").css("::text").extract()
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
        items['time'] = time
        
        yield items