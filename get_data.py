# modules
import requests
import json
import xmltodict

api_url = "https://api.entur.io/realtime/v1/rest/et?datasetId=RUT"

# fetch real-time data from bus timetables through get request
response_data = requests.get(api_url)

# convert the data to a dictionary format so we can do things with it
data_dict = xmltodict.parse(response_data.text)
# if we get an error from the line
# above, it means we have reached the
# max limit for GET requests per minute
json_url = json.dumps(data_dict)
json_url = json.loads(json_url)

# value for indexing the stop point list
stop_point_index = 0

# key indexing our way to find the stop place items
stop_point_location = json_url[
'Siri'][
'ServiceDelivery'][
'EstimatedTimetableDelivery'][
'EstimatedJourneyVersionFrame'][
'EstimatedVehicleJourney'][
0][
'EstimatedCalls'][
'EstimatedCall'][
stop_point_index][
'StopPointName']

# print the first stop place name
print(stop_point_location)