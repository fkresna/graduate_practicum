import csv
import datetime
from pymongo import MongoClient
from datetime import date

client = MongoClient()
db = client.ecommerceDB
db.promotion.delete_many({})
with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	discount = [];
	for row in reader:
		if count != 0:
			if row[6] not in discount:
				discount.append(row[6]);
		count = count + 1

for j in range(0,len(discount)-1):
	coupon_code = float(discount[j])*100	
	jsonString = {'coupon_code':coupon_code,'start_date':datetime.datetime(9,1,1),'expiry_date':'','description':'','discount_amount':discount[j]}
	result = db.promotion.insert_one(jsonString)
	print result
