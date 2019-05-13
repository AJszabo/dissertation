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
        self.conn = sqlite3.connect('url.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS origoUrl_tb""")
        self.curr.execute("""create table origoUrl_tb(
                            tags text,
                            date text,
                            title text,
                            url text
                            )""")


    def process_item(self, items, spider):
        self.store_db(items)
        return items
    
    def store_db(self,items):
        self.curr.execute("""insert into origoUrl_tb values(?,?,?,?)""",(
                repr(items['tags']),
                items['date'][0],
                items['title'][0],
                items['url'][0] 
                                    
                
        ))
        self.conn.commit()    