import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.customer_segment.find()

dw = client.ecommerceDW
#dw.customer.delete_many({})

for document in cursor:
	jsonString = {'customer_segment_id':document['customer_segment_id']}
	result = dw.customer.insert_one(jsonString)
	print result
	print jsonString
