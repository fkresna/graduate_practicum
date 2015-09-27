import csv
with open("../../rawDataSet/superstoreSalesData/order.csv") as f:
	reader = csv.reader(f)
	for row in reader:
		#Customer Name
		print row[11];
		#Province
		print row[12];
		#Region
		print row[13];
		#Customer Segment
		print row[14];

		break
