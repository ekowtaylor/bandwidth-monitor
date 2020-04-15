import time

import pyspeedtest

from config import config_manager
from util import time


# Represents the measure results
class MeasureResult:
    def __init__(self, download_rate, upload_rate, ping):
        self.download_rate = download_rate
        self.upload_rate = upload_rate
        self.ping = ping

    def print(self):
        # Import datetime module
        from datetime import date

        print()
        now = date.now()
        # Format now's date to: Month-Name Day, Year
        date = now.strftime("%B %d, %Y")
        # Format time to: Hours:Minutes:Seconds
        time = now.strftime('%H:%M:%S')
        print(f'Measure results: Date: {date}, Time: {time}')
        print(f'\tPing: {self.ping}, Download Rate:{self.download_rate}, Upload Rate: {self.upload_rate}')
        print(f'')


def get_speedtest_result() -> MeasureResult:
    speedtest = pyspeedtest.SpeedTest()
    download_rate = speedtest.download()
    upload_rate = speedtest.upload()
    ping = speedtest.ping()

    return MeasureResult(download_rate=download_rate, upload_rate=upload_rate, ping=ping)


def main():
    config_file: config_manager.ConfigFile = config_manager.get_config('config.json')
    interval = time.parse_interval(config_file.get_value('check-interval'))

    while True:
        measure_result: MeasureResult = get_speedtest_result()
        measure_result.print()
        time.sleep(interval)


if __name__ == '__main__':
    print('_______________________________________')
    print()
    print('Author: Eyal Berkovich')
    print('Description: Small Python script for measuring network\'s bandwidth')
    print()
    print('_______________________________________')

    main()
