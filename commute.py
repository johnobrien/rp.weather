import os

import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
result = gmaps.distance_matrix("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(result['rows'][0]['elements'][0]['duration'])
