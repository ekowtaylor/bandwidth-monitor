from time import sleep

from config import config_manager
from measure.measures import measure
from util import time as timeutil


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
    print()
    print('_______________________________________')

    main()
