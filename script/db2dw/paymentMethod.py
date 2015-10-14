import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.payment_method.find()

dw = client.ecommerceDW
dw.payment_method.delete_many({})

for document in cursor:
	jsonString = {'payment_method_id':document['payment_method_id'],'name':document['name']}
	result = dw.payment_method.insert_one(jsonString)
	print result
	print jsonString
