# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class WebscraperPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    
    def create_connection(self):
        self.conn = sqlite3.connect(r'C:\Users\Athan\OneDrive\Documents\Dissertation\Python\webscraperorigo\url.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS origoParagaph_tb""")
        self.curr.execute("""create table origoParagaph_tb(
                            paragaph text,
                            time text,
                            connections text,
                            start_url text
                            )""")


    def process_item(self, items, spider):
        self.store_db(items)
        return items
    
    def store_db(self,items):
        self.curr.execute("""insert into origoParagaph_tb values(?,?,?,?)""",(
                items['paragaph'][0],     
                items['time'][0],
                items['connections'][0],
                items['start_url'][0]                                 
        ))
        self.conn.commit()    