from time import sleep

from config import config_manager
from measure.measures import measure
from storage import storage_manager
from util import internet
from util import time as timeutil
from data import data_analyzer
from util.time import get_date_time

CONNECTION_TYPE = internet.get_connection_type()

time_started = None


def finish() -> None:
    data_analyzer.print_summary(time_started=time_started)
    storage_manager.close_database()

    print("[INFO]: Finished, Bye.")


def main() -> None:
    global time_started

    print()
    print('[INFO]: Reading config file: \'config.json\'')
    config_file: config_manager.ConfigFile = config_manager.get_config('config.json')
    interval = timeutil.parse_interval(config_file.get_value('check-interval'))

    storage_manager.connect()
    del config_file

    time_started = get_date_time()[6]

    print('[INFO]: Starting bandwidth measure!')
    try:
        while True:
            # Measure
            measure()

            # Pause execution for the given interval
            sleep(interval)
    except KeyboardInterrupt:
        pass
    finally:
        finish()


if __name__ == '__main__':
    print('---------------------------------------')
    print()
    print('Author: Eyal Berkovich')
    print('Description: Small tool for measuring network\'s bandwidth')
    available = internet.is_internet_available("google.com")
    print(f'Is Internet Connection Available?: {available}')
    print(f'Internet Connection Type: {CONNECTION_TYPE}')
    print()
    print('---------------------------------------')

    main()
