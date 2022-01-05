import requests
import json

# id of a stop place
stop_place_id_query = 5941

# amount of incoming buses to check for
amount_of_incomings = 1

# what we will request to the api server
query = '''{
  stopPlace(
    id: "''' + f'NSR:StopPlace:{stop_place_id_query}' + '''"
  ) {
    id
    name
    estimatedCalls(
      timeRange: 72100,
      numberOfDepartures: ''' + f"{amount_of_incomings}" + '''
    ) {
      realtime
      aimedArrivalTime
      aimedDepartureTime
      expectedArrivalTime
      expectedDepartureTime
      actualArrivalTime
      actualDepartureTime
      date
      forBoarding
      forAlighting
      destinationDisplay {
        frontText
      }
      quay {
        id
      }
      serviceJourney {
        journeyPattern {
          line {
            id
            name
            transportMode
          }
        }
      }
    }
  }
}
'''
#query.format(stop_place_id_query, amount_of_incoming_bus)

# do a POST request to api server with the assigned query
r = requests.post('https://api.entur.io/journey-planner/v3/graphql', data=query)

# convert string to dict so we can work with it
r = json.loads(r.text)

# index our way to desired data
nearest_stop_time = r['data']['stopPlace']['estimatedCalls'][0]['aimedArrivalTime']

# print the closest bus stop time
print(nearest_stop_time)

# index our way to the station name
name_of_station = r['data']['stopPlace']['name']

# print the name of the station
print(name_of_station)

id_of_station = r['data']['stopPlace']['id']
line = r['data']['stopPlace']['estimatedCalls'][0]['serviceJourney']['journeyPattern']

name_of_line = line['line']['name']
print(name_of_line)