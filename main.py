from time import sleep

from config import config_manager
from measure.measures import measure
from util import internet
from util import time as timeutil

AVAILABLE = internet.is_internet_available("google.com")


def main():
    print('Reading config file: \'config.json\'')
    config_file: config_manager.ConfigFile = config_manager.get_config('config.json')
    interval = timeutil.parse_interval(config_file.get_value('check-interval'))

    print('Starting bandwidth measure!')
    while True:
        # Measure
        measure()

        # Pause execution for the given interval
        sleep(interval)


if __name__ == '__main__':
    print('_______________________________________')
    print()
    print('Author: Eyal Berkovich')
    print('Description: Small tool for measuring network\'s bandwidth')
    print(f'Internet Connection: {AVAILABLE}')

    if not AVAILABLE:
        print('This tool is available only if internet is preset!')
        print('Closing program...')
        print()
        print('_______________________________________')
        print()
        print('Thank you, bye')
        exit()

    print()
    print('_______________________________________')

    main()
