#!/usr/bin/env python

import requests
import json

# curl -XGET  http://server/zm/api/states.json # returns list of run states
# curl -XPOST  http://server/zm/api/states/change/restart.json #restarts ZM
# curl -XPOST  http://server/zm/api/states/change/stop.json #Stops ZM
# curl -XPOST  http://server/zm/api/states/change/start.json #Starts ZM

zmBaseURI = 'http://zoneminder.com/zm'
zmAPIURI = '/'.join((zmBaseURI,'api'))
zmCheckEndpoint = '/'.join((zmAPIURI,'states.json'))
zmStartEndpoint = '/'.join((zmAPIURI,'states/change/start.json'))

currentState = requests.get(zmCheckEndpoint)
 
if currentState.status_code == 200:
    data = json.loads(currentState.text)
    print ("Active Status: ")
    print data['states'][0]['State']['isActive']
else:
   print 'An error occurred querying the API'
