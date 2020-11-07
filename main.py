import threading
from time import sleep

from config import config_manager
from data import data_analyzer
from measure.measures import measure
from storage import storage_manager
from util import internet
from util import time as timeutil
from util.time import get_date_time
from web import app

CONNECTION_TYPE = internet.get_connection_type()
WEB_PORT = 9000

time_started = None


def finish() -> None:
    data_analyzer.print_summary(time_started=time_started)
    storage_manager.close_database()

    print("[INFO]: Finished, Bye.")


def main() -> None:
    global time_started
    global WEB_PORT

    print()
    print('[INFO]: Reading config file: \'config.json\'')
    config_file: config_manager.ConfigFile = config_manager.get_config('config.json')
    interval = timeutil.parse_interval(config_file.get_value('check-interval'))
    storage_manager.DATABASE = config_file.get_value('database-name') + '.db'

    WEB_PORT = config_file.get_value('web-port')

    time_started = get_date_time()[6]

    storage_manager.connect()
    storage_manager.close_database()

    del config_file

    print('[INFO]: Starting bandwidth measure!')
    thread = threading.Thread(target=main_loop, args=(interval, ))
    thread.start()

    app.started = time_started
    app.main()


def main_loop(interval):
    try:
        while True:
            # Measure
            measure()

            # Pause execution for the given interval
            sleep(interval)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
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
