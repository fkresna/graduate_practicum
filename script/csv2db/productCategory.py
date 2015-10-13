import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
db.product_category.delete_many({})

with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	pCategories = [];
	for row in reader:
		if count != 0:
			if row[15] not in pCategories:
				pCategories.append(row[15]);
		count = count + 1
print pCategories

count = 0
for pCategory in pCategories:
	jsonString = {'product_category_id':count,'name':pCategory}
	result = db.product_category.insert_one(jsonString)
	print result;
	count = count+1
	print jsonString
