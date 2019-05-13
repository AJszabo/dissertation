# -*- coding: utf-8 -*-
import scrapy
from ..items import WebcrawlerindexItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class WebcrawlerindexhuSpider(scrapy.Spider):
    name = 'webcrawlerindexhu'
    allowed_domains = ['index.hu']
    start_urls = ["https://index.hu/24ora/?cimke=bevandorlas"]

    
    def parse(self, response):
        a = ["https://index.hu/24ora/?cimke=bevándorló",
            "https://index.hu/24ora/?cimke=bevándorlók",
            "https://index.hu/24ora/?cimke=gazdasági bevándorlók",
            "https://index.hu/24ora/?cimke=gazdasági bevándorlás",
            "https://index.hu/24ora/?cimke=gazdasági bevándorló",
            "https://index.hu/24ora/?cimke=határsértő",
            "https://index.hu/24ora/?cimke=illegális bevándorlás",
            "https://index.hu/24ora/?cimke=illegális bevándorló",
            "https://index.hu/24ora/?cimke=illegális bevándorlók",
            "https://index.hu/24ora/?cimke=menedékkérő",
            "https://index.hu/24ora/?cimke=menekült",
            "https://index.hu/24ora/?cimke=menekültek",
            "https://index.hu/24ora/?cimke=menekültválság",
            "https://index.hu/24ora/?cimke=migráció",
            "https://index.hu/24ora/?cimke=migráns",
            "https://index.hu/24ora/?cimke=migránsok"]
        for i in a:
            browser = webdriver.Chrome(r"C:\Users\Athan\OneDrive\Documents\Dissertation\Python\chromedriver")
            browser.get(i)
            items = WebcrawlerindexItem()       
            elm = browser.find_element_by_tag_name('html')
            for i in range(15):
                time.sleep(5)
                elm.send_keys(Keys.END)
            url = [""]
            urls = browser.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "rovatajanlo", " " ))]//h1//a[@href]')
            for url1 in urls:
                url1 = url1.get_attribute("href")
                url= [url1]
                items['url'] = url
                yield items
            browser.close()
    
            
