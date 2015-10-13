import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.product_category.find();
db.product_subcategory.delete_many({})
productID = []
countProduct = 0
productName = []
for document in cursor:
	productID.append(document['product_category_id']);
	productName.append(document['name']);
	countProduct = countProduct + 1
	print document

with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	pSubCategories = [];
	pCategoriesID = [];
	pSubCategoriesID = [];
	for row in reader:
		if count != 0:
			if row[16] not in pSubCategories:
				pSubCategories.append(row[16]);
				for i in range(0,countProduct):
					if row[15] == productName[i]:
						pCategoriesID.append(productID[i])
						
		count = count + 1
print pSubCategories

for j in range(0,len(pSubCategories)):
	jsonString = {'product_subcategory_id':j,'name':pSubCategories[j],'product_category_id':pCategoriesID[j]}
	result = db.product_subcategory.insert_one(jsonString)
	print result;
	print jsonString
