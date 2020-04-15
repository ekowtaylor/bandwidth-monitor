import time

import speedtest as speedtestnet

from config import config_manager
from util import time as timeutil


# Represents the measure results
class MeasureResult:
    def __init__(self, download_rate, upload_rate):
        self.download_rate = download_rate
        self.upload_rate = upload_rate

    def print(self):
        # Import datetime module
        from datetime import date

        print()
        now = date.today()
        # Format now's date to: Month-Name Day, Year
        date = now.strftime("%B %d, %Y")
        # Format time to: Hours:Minutes:Seconds
        time = now.strftime('%H:%M:%S')
        print(f'Measure results: Date: {date}, Time: {time}')
        print(f'\tDownload Rate:{self.download_rate}, Upload Rate: {self.upload_rate}')
        print(f'')


def get_speedtest_result() -> MeasureResult:
    speedtest = speedtestnet.Speedtest()
    speedtest.get_best_server()
    download_rate = speedtest.download()
    upload_rate = speedtest.upload()

    return MeasureResult(download_rate=download_rate, upload_rate=upload_rate)


def main():
    print('Reading config file: \'config.json\'')
    config_file: config_manager.ConfigFile = config_manager.get_config('config.json')
    interval = timeutil.parse_interval(config_file.get_value('check-interval'))

    print('Starting bandwidth monitor!')
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
