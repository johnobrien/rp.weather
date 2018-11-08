import schedule
import time
import threading

from update_weather import update_weather

schedule.every(1).hours.do(update_weather)


while True:
    schedule.run_pending()
    time.sleep(1)

