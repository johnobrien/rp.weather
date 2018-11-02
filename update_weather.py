# The Python script that gets the weather from the Dark Sky API
# and writes it to the epaper.
# If it runs into any problems it should fail gracefully.

import os
from datetime import date, timedelta, datetime

from darksky import forecast
from papirus import PapirusComposite

LEXINGTON = 42.4430, 71.2290

key = os.getenv("dark_sky_api_key")
if not key:
    raise Exception("DarkSky API Key not set. Set DarkSky environment variable in the local environment and try again.")

''' Possible lexington.daily.icon values:
clear-day, clear-night, rain, snow, sleet, wind, fog, cloudy, partly-cloudy-day, or partly-cloudy-night.'''

os.chdir("/home/pi/rp.weather")

def format_temp(s):
    return str("{:.0f}".format(s))+u"\u00b0"

def update_weather():
    try:

        textNImg = PapirusComposite(False)
        # os.system("sudo hwclock --hctosys")
        weekday = date.today()

        with forecast(key, *LEXINGTON) as lexington:
            long_date_name = date.strftime(weekday, '%A, %b %d')
            prefix = "./assets/icons/"
            path = prefix + lexington.currently.icon + ".bmp"
            low = None
            high = None
            for hour in lexington.hourly[6:21]:
                if low is None or hour.temperature < low:
                    low = hour.temperature
                if high is None or hour.temperature > high:
                    high = hour.temperature
            textNImg.AddText(long_date_name, 10, 0, size=22, Id="Day Name")
            try:
                textNImg.AddImg(path, 10, 25, (90,90), Id="Icon")
            except:
                textNImg.AddText(lexington.daily[0].icon, 10,25, Id="Icon")
            precipSummary = getattr(lexington.daily[0], "precipType", None)
            if hasattr(lexington.daily[0], "precipAccumulation"):
                precipSummary += ": " + "{0:.1f}".format((lexington.daily[0].precipAccumulation)) + '"'
            if precipSummary:
                offset = len(precipSummary) * 5
                textNImg.AddText(precipSummary.capitalize(), 170 - offset, 35, size=20, Id="Precipitation")
            textNImg.AddText(format_temp(low) + "-" + format_temp(high), 110, 65, size=35, Id="TempRange")
            textNImg.AddText(lexington.daily[0].summary, 10, 120, size=15, Id="Forecast")
            textNImg.AddText("5:01 PM", 10, 164, size=10, Id="Time")
            textNImg.AddText("Powered by Dark Sky", 145, 164, size=10, Id="Attribution")
            textNImg.WriteAll()
    except:
        textNImg.AddText("Error reaching Dark Sky API", 10, 10, Id="Error")
        textNImg.AddText("{0}".format(weekday), 10, 60, Id="Date")
        textNImg.WriteAll()
        raise

if __name__ == "__main__":
    update_weather()