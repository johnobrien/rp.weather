import schedule
import time
import threading

from update_weather import update_weather

# schedule.every(10).seconds.do(update_weather)
schedule.every().day.at("6:00").do(update_weather)
schedule.every().day.at("17:00").do(update_weather)


while True:
    schedule.run_pending()
    time.sleep(1)

