# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.exporters import JsonItemExporter
#
# class DriverPipeline(object):
#     def open_spider(self,spider):
#         self.file = open('driver.json','wb')
#         self.expoter = JsonItemExporter(self.file)
#         self.expoter.start_exporting()
#
#     def process_item(self, item, spider):
#         self.expoter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.file.close()
#         self.expoter.finish_exporting()
class DriverPipeline(object):
    from pymongo import MongoClient
    client = MongoClient()
    collection = client['driver']['test']
    def process_item(self,item,spider):
        self.collection.insert(item)
        return item