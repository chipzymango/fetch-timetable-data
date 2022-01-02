import requests
import json

# what we will request to the api server
query = """{
  stopPlace(
    id: "NSR:StopPlace:5952" 
  ) {
    id
    name
    estimatedCalls(
      timeRange: 72100,
      numberOfDepartures: 3
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
}"""

# do a POST request to api server with the assigned query
r = requests.post('https://api.entur.io/journey-planner/v3/graphql', data=query)

# convert string to dict so we can work with it
r = json.loads(r.text)

# index our way to desired data
nearest_stop_time = r['data']['stopPlace']['estimatedCalls'][0]['aimedArrivalTime']

# print the closest bus stop time
print(nearest_stop_time)