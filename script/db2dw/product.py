import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.product.find()

dw = client.ecommerceDW
dw.product.delete_many({})

for document in cursor:
	jsonString = {'product_id':document['product_id'],'category_id':document['category_id'],'subcategory_id':document['subcategory_id'],'name':document['name']}
	result = dw.product.insert_one(jsonString)
	print result
	print jsonString
