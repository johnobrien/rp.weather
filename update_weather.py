# The Python script that gets the weather from the Dark Sky API
# and writes it to the epaper.
# If it runs into any problems it should fail gracefully.

import os
from darksky import forecast
from datetime import date, timedelta, datetime

from papirus import PapirusComposite

LEXINGTON = 42.4430, 71.2290

key = os.getenv("dark_sky_api_key")
if not key:
    raise Exception("DarkSky API Key not set. Set DarkSky environment variable in the local environment and try again.")

''' Possible lexington.daily.icon values:
clear-day, clear-night, rain, snow, sleet, wind, fog, cloudy, partly-cloudy-day, or partly-cloudy-night.'''

def format_temp(s):
    return str("{:.0f}".format(s))+u"\u00b0"

try:
    textNImg = PapirusComposite(False)
    weekday = date.today()

    with forecast(key, *LEXINGTON) as lexington:
        long_date_name = date.strftime(weekday, '%A, %b %d')
        lexington.refresh()
        prefix = "./assets/icons/"
        path = prefix + lexington.daily.icon + ".bmp"
        low = lexington.daily.data[0]["apparentTemperatureLow"]
        high = lexington.daily.data[0]["apparentTemperatureHigh"]
        textNImg.AddText(long_date_name, 10, 0, size=22, Id="Day Name")
        textNImg.AddImg(path, 10, 25, (90,90), Id="Icon")
        textNImg.AddText(format_temp(low) + "-" + format_temp(high), 110, 50, size=35)
        textNImg.AddText(lexington.hourly.summary, 10, 120, size=15, Id="Forecast")
        textNImg.WriteAll()
except:
    textNImg.AddText("Error reaching Dark Sky API", 10, 10, Id="Error")
    textNImg.AddText("Please check the internet settings.", 10, 20, Id="Error")
    textNImg.WriteAll()
    raise
