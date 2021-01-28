# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from itemadapter import ItemAdapter
from .secrets import password, user, database

class MongodbPipeline:
    collection_name = "globo_news"


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.tsc5b.mongodb.net/{database}?retryWrites=true&w=majority")
        self.db = self.client["timeline"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.db[self.collection_name].insert(item)
        except pymongo.errors.DuplicateKeyError:
            print(f"{item} is alredy on database")
