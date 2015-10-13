import csv
from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.product_category.find();
db.product.delete_many({})
productCategoryID = []
countCategory = 0
productCategoryName = []
for document in cursor:
        productCategoryID.append(document['product_category_id']);
        productCategoryName.append(document['name']);
        countCategory = countCategory + 1
print productCategoryName[0]

cursor2 = db.product_subcategory.find();
productSubCategoryID = []
productSubCategoryName = []
countSubCategory = 0
for document2 in cursor2:
	productSubCategoryID.append(document2['product_subcategory_id']);
	productSubCategoryName.append(document2['name']);
	countSubCategory = countSubCategory + 1
	print document2

with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	count = 0
	pName = [];
	pCategoryID = [];
	pSubcategoryID = [];
	for row in reader:
		if count != 0:
			if row[17] not in pName:
				pName.append(row[17]);
				for i in range(0,countCategory):
					if row[15] == productCategoryName[i]:
						pCategoryID.append(productCategoryID[i]) 
				
				for j in range(0,countSubCategory):
					if row[16] == productSubCategoryName[j]:
						pSubcategoryID.append(productSubCategoryID[j])
				count = count + 1				
		else:
			count = count + 1
print count
print len(pName)
print len(pCategoryID)
print len(pSubcategoryID)
for k in range(0,len(pName)-1):
	jsonString = {'product_id':k,'category_id':pCategoryID[k],'subcategory_id':pSubcategoryID[k],'name':pName[k]}
	result = db.product.insert_one(jsonString)
	print result;
	print jsonString
