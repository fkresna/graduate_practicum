import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
db.payment_status.delete_many({})

payment_status = ["paid","refund","chargeback","pending","authorized","fail","declined"]
count = 0
for payment in payment_status:
	jsonString = {'payment_status_id':count,'name':payment}
	result = db.payment_status.insert_one(jsonString)
	print result;
	count = count+1
	print jsonString
