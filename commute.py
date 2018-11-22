import os

import googlemaps
import datetime


gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))

today = datetime.datetime.today()

arrival_time = datetime.datetime.replace(today, hour=9)

# Currently not working...
print(arrival_time)

result = gmaps.distance_matrix(origins=os.getenv('HOME_POSTAL_ADDRESS'),
                                     destinations=os.getenv('WORK_POSTAL_ADDRESS'),
                                     mode="driving",
                                     arrival_time=arrival_time)

secs = result['rows'][0]['elements'][0]['duration']['value']
