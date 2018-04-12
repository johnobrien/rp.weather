# The Python script that gets the weather from the Dark Sky API
# and writes it to the epaper.
# If it runs into any problems it should fail gracefully.

import os
from darksky import forecast
from datetime import date, timedelta, datetime

LEXINGTON = 42.4430, 71.2290

try:
    from papirus import PapirusComposite
except ModuleNotFoundError:
    ## The papirus module is not installed
    ## so let's use a dummy class for it that
    ## prints out to stdout instead
    class PapirusText:
        def write(self, text):
            print("{0}".format(text))

key = os.getenv("dark_sky_api_key")
if not key:
    raise Exception("DarkSky API Key not set. Set DarkSky environment variable in the local environment and try again.")

output = ""

''' Possible day.icon values:
clear-day, clear-night, rain, snow, sleet, wind, fog, cloudy, partly-cloudy-day, or partly-cloudy-night.'''

try:
    weekday = date.today()
    with forecast(key, *LEXINGTON) as boston:
        for day in boston.daily[0:3]:
            day = dict(day=date.strftime(weekday, '%a'),
                       icon=day.icon,
                       tempMin=round(day.temperatureMin),
                       tempMax=round(day.temperatureMax)
                       )
            output += ('{day}: {icon} \n'.format(**day))
            weekday += timedelta(days=1)
    # output += 'Last Updated: {0}'.format(datetime.now())

    textNImg = PapirusComposite(False)
    textNImg.AddImg('/assets/icons/cloud.bmp', Id="Top")
    textNImg.WriteAll()
except:
    # Couldn't access Dark Sky, so fail gracefully
    # probably writing to a log.
    raise
