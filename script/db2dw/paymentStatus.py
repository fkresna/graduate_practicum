import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.payment_status.find()

dw = client.ecommerceDW
dw.payment_status.delete_many({})

for document in cursor:
	jsonString = {'payment_status_id':document['payment_status_id'],'name':document['name']}
	result = dw.payment_status.insert_one(jsonString)
	print result
	print jsonString
