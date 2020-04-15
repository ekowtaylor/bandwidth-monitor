from time import sleep, gmtime, strftime

import speedtest as speedtestnet

from config import config_manager
from util import time as timeutil


# Represents the measure results
class MeasureResult:
    def __init__(self, ping_rate, download_rate, upload_rate, date, time):
        self.ping_rate = ping_rate
        self.download_rate = download_rate
        self.upload_rate = upload_rate
        self.date = date
        self.time = time

    def print(self):
        print()

        print(f'Measure results: Date: {self.date}, Time: {self.time}')
        print(
            f'\tPing Rate: {self.ping_rate} Download Rate: {self.download_rate // 1000000}, Upload Rate: {self.upload_rate // 1000000}')
        print(f'')


def get_speedtest_result() -> MeasureResult:
    # Import datetime module
    from datetime import date

    now = date.today()
    # Format now's date to: Month-Name Day, Year
    current_date = now.strftime("%B %d, %Y")
    # Format time to: Hours:Minutes:Seconds
    current_time = strftime('%H:%M:%S', gmtime())

    speedtest = speedtestnet.Speedtest()
    speedtest.get_best_server()
    download_rate = speedtest.download()
    upload_rate = speedtest.upload()
    ping_rate = speedtest.results.ping

    return MeasureResult(download_rate=download_rate, upload_rate=upload_rate, ping_rate=ping_rate, date=current_date,
                         time=current_time)


def main():
    print('Reading config file: \'config.json\'')
    config_file: config_manager.ConfigFile = config_manager.get_config('config.json')
    interval = timeutil.parse_interval(config_file.get_value('check-interval'))

    print('Starting bandwidth monitor!')
    while True:
        # Get measure results from speedtest.net
        measure_result: MeasureResult = get_speedtest_result()
        # Print measure results
        measure_result.print()

        # Pause execution for the given interval
        sleep(interval)


if __name__ == '__main__':
    print('_______________________________________')
    print()
    print('Author: Eyal Berkovich')
    print('Description: Small tool for measuring network\'s bandwidth')
    print()
    print('_______________________________________')

    main()
