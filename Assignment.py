
import datetime
import requests
import bs4
import json
date_format='%Y-%m-%d'
isValid=True
while isValid:
	start_date=str(input("Enter Date in YYYY-MM-DD:"))
	try:
		date_obj=datetime.datetime.strptime(start_date,date_format)
		print(date_obj.date())
		start_date=str(date_obj.date())
		isValid=False
	except:
		print("Incorrect Format should be YYYY-MM-DD")
isValid=True
while isValid:
	end_date=str(input("Enter Date in YYYY-MM-DD:"))
	try:
		date_obj=datetime.datetime.strptime(end_date,date_format)
		print(date_obj.date())
		end_date=str(date_obj.date())
		isValid=False
	except:
		print("Incorrect Format should be YYYY-MM-DD")

result=requests.get("https://api.urassistant.me/v1/assistant/results/json/get?apikey=TORUWZENLVUW&fromdate="+start_date+"8&todate="+end_date+"&sourcecode=test&sourceloc=assistanturstaging")
#print(result.json())
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

result=result.json()
venue_details=result['uv']['data']['venues']
events=result['uv']['data']['events']
print(venue_details['VEN1103']['info']['city'])
print(type(events))
data={}

data["total_events"]=str(len(events))
event=[]
venue={}
for index in events:
	event_info={}
	event_info["event_name"]=index['eventname']
	event_info["tickets_url"]=index['ticketsurl']
	event_info["tables_url"]=index['tablesurl']
	event_info["event_date"]=index['caldate']
	event_info["opening_hours"]=index['opentime']
	event_info["closing_hours"]=index['closetime']
	venue_code=index['venuecode']
	print(venue_details[venue_code]['info']['city'])
	venue["venue_name"]=venue_details[venue_code]['info']['name']
	venue["venue_desc"]=venue_details[venue_code]['info']['descr']
	venue_contact_info={}
	operating_days={}
	venue_contact_info["address"]=venue_details[venue_code]['info']['address']
	venue_contact_info["city"]=venue_details[venue_code]['info']['city']
	venue_contact_info["zip"]=venue_details[venue_code]['info']['zip']
	venue_contact_info["phone"]=venue_details[venue_code]['info']['phone']
	operating_days["Monday"]=venue_details[venue_code]['ophours']['weekdays']['1']['state']
	
	operating_days["Tuesday"]=venue_details[venue_code]['ophours']['weekdays']['2']['state']
	operating_days["Wednesday"]=venue_details[venue_code]['ophours']['weekdays']['3']['state']
	operating_days["Thursday"]=venue_details[venue_code]['ophours']['weekdays']['4']['state']
	operating_days["Friday"]=venue_details[venue_code]['ophours']['weekdays']['5']['state']
	operating_days["Saturday"]=venue_details[venue_code]['ophours']['weekdays']['6']['state']
	operating_days["Sunday"]=venue_details[venue_code]['ophours']['weekdays']['7']['state']

	venue["venue_contact_info"]=venue_contact_info
	venue["operating_days"]=operating_days
	event_info["venue"]=venue
	event.append(event_info)
data["events"]=event
print(data)
writeToJSONFile('./','output',data)





