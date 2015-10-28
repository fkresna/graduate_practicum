from pymongo import MongoClient

client = MongoClient()
db = client.ecommerceDB
cursor = db.customer.find()

dw = client.ecommerceDW
dw.country.delete_many({})

count = 0
countryName = [];
countryISOCode = []
province = []
region = []
for document in cursor:
	if (document['province'] not in province) or (document['region'] not in region):
		province.append(document['province'])
		region.append(document['region'])
		if document['country'] == 'CA':
			countryName.append("Canada")
		else:
			countryName.append("")
		countryISOCode.append('CA')
		
for j in range(0,len(province)-1):
	jsonString = {'country_id':count,'country_name':countryName[j],'province':province[j],'region':region[j],'country_ISO_code':countryISOCode[j],'country_name':countryName[j]}
	print jsonString
	count = count +1
