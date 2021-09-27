import time
import pandas as pd
from pathlib import Path
from pathlib import PurePath
from os import walk

from models import DimDate
from models import FactMaintenanceContractorPayment
from dbhelper import DatabaseHelper
from weatherhelper import WeatherFetcher
import log

# set up logger
logger = log.setup_logger('root')

def main():
    # using timer or operating system Cron Job are better ways to do this
    while True:
        weather_info = WeatherFetcher.getCurrentSydneyWeather()
        logger.debug(weather_info.json_data)
        if weather_info.success:
            weather_info.transform()
            weather_info.load()
        DatabaseHelper.getInstance().close()
        logger.debug("sleeping for 3600 seconds")
        time.sleep(60*60)

if __name__ == "__main__":
    main()  
