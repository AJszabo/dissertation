# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class NegynegynegyarticlesPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    
    def create_connection(self):
        self.conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS negynegynegyUrl_tb""")
        self.curr.execute("""create table negynegynegyUrl_tb(
                            url text
                            )""")


    def process_item(self, items, spider):
        self.store_db(items)
        return items
    
    def store_db(self,items):
        self.curr.execute("""insert into negynegynegyUrl_tb values(?)""",(
                items['url'][0],
                                   
                
        ))
        self.conn.commit()   