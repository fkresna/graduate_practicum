import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
db.payment_method.delete_many({})

payment_methods = ["visa","mastercard","paypal"]
count = 0
for payment in payment_methods:
	jsonString = {'payment_method_id':count,'name':payment}
	result = db.payment_method.insert_one(jsonString)
	print result;
	count = count+1
	print jsonString
