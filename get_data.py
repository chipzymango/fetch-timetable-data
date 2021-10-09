# modules
import requests
import json
import xmltodict

# fetch real-time data from bus timetables through get request
response_data = requests.get("https://api.entur.io/realtime/v1/rest/et?datasetId=RUT")

# get the data in dictionary format
data_dict = xmltodict.parse(response_data.text)
json_url = json.dumps(data_dict)

print(json_url)