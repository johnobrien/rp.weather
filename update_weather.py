# The Python script that gets the weather from the Dark Sky API
# and writes it to the epaper.
# If it runs into any problems it should fail gracefully.

import os
from darksky import forecast
import datetime

LEXINGTON = 42.4430, 71.2290

try:
    from papirus import PapirusText
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

text = PapirusText()
try:
    with forecast(key, *LEXINGTON) as lexington:
        text.write("{0}\nLast updated:{1}".format(lexington.daily.summary, datetime.datetime.now()))

except:
    # Couldn't access Dark Sky, so fail gracefully
    # probably writing to a log.
    raise
