import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.shipping.find()

dw = client.ecommerceDW
dw.shipping.delete_many({})

for document in cursor:
	jsonString = {'shipping_id':document['shipping_id'],'name':document['name']}
	result = dw.shipping.insert_one(jsonString)
	print result
	print jsonString
