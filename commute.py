import os

import googlemaps
import datetime


def commute():
    gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))

    today = datetime.datetime.today()

    arrival_time = datetime.datetime.replace(today, hour=9, minute=00)

    result = gmaps.distance_matrix(origins=os.getenv('HOME_POSTAL_ADDRESS'),
                                   destinations=os.getenv('WORK_POSTAL_ADDRESS'),
                                   mode="driving",
                                   arrival_time=arrival_time)

    secs = result['rows'][0]['elements'][0]['duration']['value']

    departure_time = arrival_time - datetime.timedelta(seconds=secs)

    return "{d.hour}:{d.minute:02}".format(d=departure_time)
