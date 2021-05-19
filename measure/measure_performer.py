from typing import Tuple

from util import internet
from util import time

import psutil

import speedtest as speedtestnet

from measure.measure_result import MeasureResult

import traceback


def perform_measure(measure_result: MeasureResult):
    connection_type = internet.get_connection_type()
    connection_available = internet.is_internet_available(measure_result.source)
    month, day, year, hours, minutes, seconds, milliseconds = time.get_date_time()

    measure_result.connection_available = connection_available
    measure_result.connection_type = connection_type
    measure_result.year = year
    measure_result.month = month
    measure_result.day = day
    measure_result.timestamp = milliseconds
    measure_result.hour = hours
    measure_result.minutes = minutes
    measure_result.seconds = seconds 

    if not connection_available:
        measure_result.download_rate = 0.0
        measure_result.upload_rate = 0.0
        measure_result.ping_rate = -1

        return

    if measure_result.source == 'fast.com':
        download_rate, upload_rate, ping_rate = perform_fastcom_measure(measure_result=measure_result)

    elif measure_result.source == 'speedtest.net':
        download_rate, upload_rate, ping_rate = perform_speedtest_measure()

        measure_result.download_rate = download_rate
        measure_result.upload_rate = upload_rate
        measure_result.ping_rate = ping_rate


def perform_speedtest_measure():
        '''
            Returns a tuple that includes the values of the internet measured rates
        '''

        try:
            speedtest = speedtestnet.Speedtest()
            speedtest.get_best_server()
            download_rate = speedtest.download()
            upload_rate = speedtest.upload()
            ping_rate = speedtest.results.ping

            return (download_rate, upload_rate, ping_rate)

        except Exception as e:
            traceback.print_exc()
            # If any exception has occured, we return failed values for the connection.
            return 0, 0, -1


# TODO: Implement fast.com measurement
def perform_fastcom_measure(measure_result: MeasureResult):
    return 0, 0, -1


# TODO: Get process list for each measure we perform.
def get_process_list():
    pass
