from measure.measure_result import MeasureResult
from measure.measure_performer import perform_measure

from storage import storage_manager

def measure():
    # Get measure results from speedtest.net and fast.com
    speedtest_measure_result = MeasureResult('speedtest.net')
    fastcom_measure_result = MeasureResult('fast.com')

    # Call measure perform
    perform_measure(measure_result=speedtest_measure_result)
    perform_measure(measure_result=fastcom_measure_result)

    speedtest_measure_result.parse_rates()
    fastcom_measure_result.parse_rates()
    
    # Store measure results
    storage_manager.store_measure_result(speedtest_measure_result)
    storage_manager.store_measure_result(fastcom_measure_result)

    # Print measure results
    fastcom_measure_result.print()
    speedtest_measure_result.print()
