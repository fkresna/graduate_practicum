import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
db.customer_segment.delete_many({})
with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	custSegment = [];
	for row in reader:
		if count != 0:
			if row[14] not in custSegment:
				custSegment.append(row[14]);
		count = count + 1
print custSegment

count = 0
for segment in custSegment:
	jsonString = {'customer_segment_id':count,'name':segment}
	result = db.customer_segment.insert_one(jsonString)
	print result;
	count = count+1

