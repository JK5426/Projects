# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

class ImdbPipeline(object):
    #It is a class method and the main purpose of this mrthos is to 
    #grab whatever value want from those settings.py
    @classmethod
    def from_crawler(cls,crawler):
        logging.warning(crawler.settings.get("Mongo_uri"))

    def open_spider(self,spider):
        logging.warning("Spider is open from Pipeline.")

    def close_spider(self,spider):
        logging.warning("Spider is closed from Pipeline.")

    def process_item(self, item, spider):
        return item
