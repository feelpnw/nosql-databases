import pymongo
from pymongo import MongoClient

client = MongoClient()
database = client.store

collection = database.sales
# sale = {}
# sale["item"] = "product1"
# sale["year"] = 2016
# sale["price"] = 200
# collection.insert(sale)

a = collection.find({"item": "product1"}).count()
print(a)
cursor = collection.find()
# print(sale["item"])
print(cursor)