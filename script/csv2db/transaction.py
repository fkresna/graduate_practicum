import csv
import time
import datetime
from pymongo import MongoClient
from datetime import date

client = MongoClient()
db = client.ecommerceDB
db.transaction.delete_many({})

custID = []
custName = []
cCustomer = db.customer.find()
for document in cCustomer:
	custID.append(document['customer_id']);
	custName.append(document['name']);

shipID = []
shipName = []
cShipping = db.shipping.find()
for document in cShipping:
	shipID.append(document['shipping_id'])	
	shipName.append(document['name'])

'''
affID = []
affName = []
cAffiliate = db.affiliate.find()
for document in cAffiliate:
	affID.append(document['affiliate_id'])
	affName.append(document['name'])
'''

payStatusID = []
payName = []
cPaymentStatus = db.payment_status.find()
for document in cPaymentStatus:
	payStatusID.append(document['payment_status_id'])
	payName.append(document['name'])

payMethodID = []
payMethodName = []
cPaymentMethod = db.payment_method.find()
for document in cPaymentMethod:
	payMethodID.append(document['payment_method_id'])
	payMethodName.append(document['name'])
print payMethodID
print payMethodName

'''
promoCouponCode = []
cPromotion = db.payment_method.find()
for document in cPromotion:
	promoCouponCode.append(document['coupon_code'])
'''

with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
        count = 0
	transactionID = []
	tanggal = []
	countryID = []
	paymentMethodID = []
	customerID = []
	paymentStatusID = []
	affiliateID = []
	couponCode = []
	shippingID = []
	totalPrice = []
	shippingCost = []
	ipAddress = []
	userAgent = []
	riskScore = []
	for row in reader:
		if count != 0:
			#row[1]:transaction_id
			if row[1] not in transactionID:
				transactionID.append(row[1])
				#row[2]:order date
				tanggal.append(row[2])
				#row[5]:sales
				totalPrice.append(row[5])
			else:
				#find the same transactionID
				indexID = transactionID.index(row[1])
				totalPrice[indexID] = totalPrice[indexID] + row[5]
		count = count + 1

for k in range(0,len(transactionID)-1):
	temp = tanggal[k].split('/')
	temp[2] = '20'+temp[2]
	jsonString = {'transaction_id':transactionID[k],'date':datetime.datetime(int(temp[2]),int(temp[0]),int(temp[1]))}
	result = db.transaction.insert_one(jsonString)
	print result
	print jsonString
