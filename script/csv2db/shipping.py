import csv
from pymongo import MongoClient

with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	shippings = [];
	for row in reader:
		if count != 0:
			if row[7] not in shippings:
				shippings.append(row[7]);
		count = count + 1
print shippings
client = MongoClient()
db = client.ecommerceDB

count = 0
for shipping in shippings:
	jsonString = {'customer_id':count,'name':shipping}
	result = db.customer_segment.insert_one(jsonString)
	print result;
	count = count+1
	print jsonString
