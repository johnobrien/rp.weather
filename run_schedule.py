import schedule
import time, functools

def catch_exceptions():
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
        return wrapper
    return catch_exceptions_decorator


from update_weather import update_weather

uw = catch_exceptions(update_weather)


schedule.every().day.at("6:00").do(uw)
schedule.every().day.at("7:00").do(uw)
schedule.every().day.at("8:00").do(uw)
schedule.every().day.at("9:00").do(uw)
schedule.every().day.at("10:00").do(uw)
schedule.every().day.at("11:00").do(uw)
schedule.every().day.at("12:00").do(uw)
schedule.every().day.at("13:00").do(uw)
schedule.every().day.at("14:00").do(uw)
schedule.every().day.at("15:00").do(uw)
schedule.every().day.at("16:00").do(uw)
schedule.every().day.at("17:00").do(uw)
schedule.every().day.at("18:00").do(uw)
schedule.every().day.at("19:00").do(uw)
schedule.every().day.at("20:00").do(uw)
schedule.every().day.at("21:00").do(uw)
schedule.every().day.at("22:00").do(uw)


while True:
    uw()
    schedule.run_pending()
    time.sleep(1)



