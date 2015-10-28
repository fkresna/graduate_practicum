import csv
import json, ast
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.customer_segment.find()
db.customer.delete_many({})
cCS = 0
csID = []
csName = []
for document in cursor:
	csID.append(document['customer_segment_id']);
	csName.append(document['name']);
	cCS = cCS + 1
	print document

with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	unique = 0
	name = []
	province = []
	region = []
	segment = []
	email = []
	for row in reader:
		if count != 0:
			if row[11] not in name:
				name.append(row[11])
				province.append(row[12]);
				region.append(row[13]);
				for i in range(0,cCS-1):
					if row[14] == csName[i]:
						segment.append(csID[i])
				email.append(row[11].replace(" ", "").lower()+"@gmail.com");
				unique = unique + 1
		count = count + 1

for j in range(0,count-1):
	jsonString = {'customer_id':j,'customer_group_id':segment[j],'name':name[j],'email_address':email[j],'province':province[j],'region':region[j],'country':'CA'}
	result = db.customer.insert_one(jsonString)
	print result
print count
