# -*- coding: utf-8 -*-
import scrapy
from ..items import Webscraper24HuItem
import sqlite3

class A24huacrticleurlsSpider(scrapy.Spider):
    name = '24huacrticleurls'
    allowed_domains = ['24.hu']
    conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
    curr = conn.cursor()
    urls=[]
    curr.execute("""SELECT url FROM 'huszonnegyhuUrl_tb' WHERE
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
                 url LIKE "%2014/12%" ORDER BY url;""")
    for row in curr.fetchall():
        urlrow = str(row)
        urlrow = urlrow.replace('(',"")
        urlrow = urlrow.replace(')',"")
        urlrow = urlrow.replace("'","")
        urlrow = urlrow.replace(',',"")
        urls.append(urlrow)
    start_urls = urls
    
    def parse(self, response):
        urls = response.css('.post-body').extract()
        items = Webscraper24HuItem()
        text = ['']
        connections = ['']
        time = ['']
        start_url = ['']
        for url in urls:
            tags = response.css(".post-body p::text,.post-body.highlight-block::text, .livepost-event-body p::text, .post-body a::text").extract()
            connection = response.css(".post-body a").xpath("@href").extract()
            time = response.css(".m-author__wrapCatDateTitulus::text").extract()
            for paragaph in tags:
                text[0] += " " + paragaph
            for co in connection:
                connections[0] += " " + co
            start_url[0] = response.request.url
            
            items['paragaph'] = text
            items['time'] = time
            items['connections'] = connections
            items['start_url'] = start_url
            
            yield items


