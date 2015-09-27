from pymongo import MongoClient

client = MongoClient()
db = client.test

#all document, like select *
#cursor = db.restaurants.find();

#for document in cursor:
#	print(document)

#with condition
cursor = db.restaurants.find({"borough":"Manhattan"})

for document in cursor:
	print(document)
