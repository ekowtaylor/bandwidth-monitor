import speedtest as speedtestnet

from measure.measure_result import MeasureResult
from storage import storage_manager
from util import internet
from util import time

# TODO: Implement fast.com measure result
def get_fastcom_result() -> MeasureResult:
    source = 'fast.com'

    month, day, year, hours, minutes, seconds, milliseconds = time.get_date_time()

    download_rate = 0
    upload_rate = 0
    ping_rate = 0

    result = MeasureResult(connection_available=False, connection_type="Not implemented yet",
                           download_rate=download_rate, upload_rate=upload_rate, ping_rate=ping_rate,
                           month=month, day=day, year=year, minutes=minutes, hour=hours, seconds=seconds,
                           timestamp=milliseconds, source=source)

    return result


def get_speedtest_result() -> MeasureResult:
    connection_type = "None"
    connection_available = internet.is_internet_available("google.com")
    source = 'speedtest.net'
    month, day, year, hours, minutes, seconds, milliseconds = time.get_date_time()
    result = None

    if connection_available:
        try:
            connection_type = internet.get_connection_type()
            speedtest = speedtestnet.Speedtest()
            speedtest.get_best_server()
            download_rate = speedtest.download()
            upload_rate = speedtest.upload()
            ping_rate = speedtest.results.ping
            result = MeasureResult(connection_available=connection_available, connection_type=connection_type,
                                   download_rate=download_rate, upload_rate=upload_rate, ping_rate=ping_rate,
                                   month=month, day=day, year=year, minutes=minutes, hour=hours, seconds=seconds,
                                   timestamp=milliseconds, source=source)
        except:
            if not internet.is_internet_available("google.com"):
                connection_available = False

    if not connection_available:
        result = MeasureResult(connection_available=connection_available, connection_type=connection_type,
                               download_rate=0, upload_rate=0, ping_rate=-1, month=month, day=day, year=year,
                               minutes=minutes, hour=hours, seconds=seconds, source=source, timestamp=milliseconds)

    return result


def measure():
    # Get measure results from speedtest.net
    speedtest_measure_result: MeasureResult = get_speedtest_result()
    fastcom_measure_result: MeasureResult = get_fastcom_result()

    # Store measure results
    storage_manager.store_measure_result(speedtest_measure_result)
    storage_manager.store_measure_result(fastcom_measure_result)

    # Print measure results
    fastcom_measure_result.print()
    speedtest_measure_result.print()
