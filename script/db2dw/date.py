import csv
from pymongo import MongoClient

client = MongoClient()
dw = client.ecommerceDW
dw.date.delete_many({})

with open("../../rawDataSet/date_dimension.csv") as f:
	reader = csv.reader(f)
	count = 0
	dateKey = []
	fullDate = []
	dayOfWeek = []
	dayNumOfWeek = []
	dayNumOverall = []
	dayName = []
	dayAbbrev = []
	weekdayFlag = []
	weekNumInYear = []
	weekNumOverall = []
	weekBeginDate = []
	weekBeginDateKey = []
	month = []
	monthNumOverall = []
	monthName = []
	monthAbbrev = []
	quarter = []
	year = []
	yearmo = []
	fiscalMonth = []
	fiscalQuarter = []
	fiscalYear = []
	monthEndFlag = []
	sameDayYearAgo = []
	for row in reader:
		if count !=0:
			dateKey.append(row[0])
			fullDate.append(row[1])
			dayOfWeek.append(row[2])
			dayNumOfWeek.append(row[3])
			dayNumOverall.append(row[4])
			dayName.append(row[5])
			dayAbbrev.append(row[6])
			weekdayFlag.append(row[7])
			weekNumInYear.append(row[8])
			weekNumOverall.append(row[9])
			weekBeginDate.append(row[10])
			weekBeginDateKey.append(row[11])
			month.append(row[12])
			monthNumOverall.append(row[13])
			monthName.append(row[14])
			monthAbbrev.append(row[15])
			quarter.append(row[16])
			year.append(row[17])
			yearmo.append(row[18])
			fiscalMonth.append(row[19])
			fiscalQuarter.append(row[20])
			fiscalYear.append(row[21])
			monthEndFlag.append(row[22])
			sameDayYearAgo.append(row[23])
		count = count + 1

for i in range(0,len(dateKey)-1):
	jsonString = {'date_key':dateKey[i],'full_date':fullDate[i],'day_of_week':dayOfWeek[i],'day_num_of_week':dayNumOfWeek[i],'day_num_overall':dayNumOverall[i],'day_name':dayName[i],'day_abbrev':dayAbbrev[i],'weekday_flag':weekdayFlag[i],'week_num_in_year':weekNumInYear[i],'week_num_overall':weekNumOverall[i],'week_begin_date':weekBeginDate[i],'week_begin_date_key':weekBeginDateKey[i],'month':month[i],'month_num_overall':monthNumOverall[i],'month_name':monthName[i],'month_abbrev':monthAbbrev[i],'quarter':quarter[i],'year':year[i],'yearmo':yearmo[i],'fiscal_month':fiscalMonth[i],'fiscal_quarter':fiscalQuarter[i],'fiscal_year':fiscalYear[i],'month_end_flag':monthEndFlag[i],'same_day_year_ago':sameDayYearAgo[i]}
	print jsonString
	result = dw.date.insert_one(jsonString)
	print result
