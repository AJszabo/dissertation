# -*- coding: utf-8 -*-
import scrapy
from ..items import VshuwebcrawlerItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class WebcrawlervshuSpider(scrapy.Spider):
    name = 'webcrawlervshu'
    allowed_domains = ['vs.hu']
    start_urls = ["https://vs.hu/cimke/bevandorlas"]
    
    def parse(self, response):
         browser = webdriver.Chrome(r"C:\Users\Athan\OneDrive\Documents\Dissertation\Python\chromedriver")
         a = ["https://vs.hu/cimke/bevandorlas",
            "https://vs.hu/cimke/bevandorlo",
            "https://vs.hu/cimke/bevandorlok",
            "https://vs.hu/cimke/gazdasagi bevandorlok",
            "https://vs.hu/cimke/gazdasagi bevandorlo",
            "https://vs.hu/cimke/gazdasagi bevandorlas",
            "https://vs.hu/cimke/hatarserto",
            "https://vs.hu/cimke/illegalis bevandorlas",
            "https://vs.hu/cimke/illegalis bevandorlo",
            "https://vs.hu/cimke/illegalis bevandorlok",
            "https://vs.hu/cimke/menedekkero",
            "https://vs.hu/cimke/menekult",
            "https://vs.hu/cimke/menekultek",
            "https://vs.hu/cimke/menekultvalsag",
            "https://vs.hu/cimke/migracio",
            "https://vs.hu/cimke/migrans",
            "https://vs.hu/cimke/migransok"]
         for i in a:
            browser.get(i)
            items = VshuwebcrawlerItem()       
            elm = browser.find_element_by_tag_name('html')
            for i in range(15):
                time.sleep(5)
                elm.send_keys(Keys.END)
            url = [""]
            urls = browser.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "column", " " ))]//a[@href]')
            for url1 in urls:
                url1 = url1.get_attribute("href")
                url= [url1]
                items['url'] = url
                yield items
            

        