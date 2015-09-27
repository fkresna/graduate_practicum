from pymongo import MongoClient
client = MongoClient()
db = client.primer
db.dataset
coll = db.dataset

print "Hello"
