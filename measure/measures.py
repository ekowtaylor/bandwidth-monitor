from time import gmtime, strftime

import speedtest as speedtestnet

from measure.measure_result import MeasureResult


def get_fastcom_result() -> MeasureResult:
    source = 'fast.com'
    current_date, current_time = get_date_time()

    download_rate = 0
    upload_rate = 0
    ping_rate = 0

    return MeasureResult(download_rate=download_rate, upload_rate=upload_rate, ping_rate=ping_rate, date=current_date,
                         time=current_time, source=source)


def get_speedtest_result() -> MeasureResult:
    source = 'speedtest.net'
    current_date, current_time = get_date_time()

    speedtest = speedtestnet.Speedtest()
    speedtest.get_best_server()
    download_rate = speedtest.download()
    upload_rate = speedtest.upload()
    ping_rate = speedtest.results.ping

    return MeasureResult(download_rate=download_rate, upload_rate=upload_rate, ping_rate=ping_rate, date=current_date,
                         time=current_time, source=source)


def get_date_time():
    # Import datetime module
    from datetime import date
    now = date.today()
    # Format now's date to: Month-Name Day, Year
    current_date = now.strftime("%B %d, %Y")
    # Format time to: Hours:Minutes:Seconds
    current_time = strftime('%H:%M:%S', gmtime())
    return current_date, current_time


def measure():
    # Get measure results from speedtest.net
    measure_result: MeasureResult = get_speedtest_result()

    # Print measure results
    measure_result.print()
