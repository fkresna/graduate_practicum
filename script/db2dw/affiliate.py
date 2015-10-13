import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.affiliate.find()

dw = client.ecommerceDW
dw.affiliate.delete_many({})

for document in cursor:
	jsonString = {'affiliate_id':document['affiliate_id']}
	result = dw.affiliate.insert_one(jsonString)
	print result
	print jsonString
