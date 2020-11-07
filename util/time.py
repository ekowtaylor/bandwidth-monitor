from time import gmtime, strftime

intervals = {
    'w': 60 * 60 * 24 * 7,
    'd': 60 * 60 * 24,
    'h': 60 * 60,
    'm': 60,
    's': 1
}


def parse_interval(time: str):
    time = time.lower()
    last_char = time[len(time) - 1]
    interval_time = 1

    if not last_char.isnumeric():
        interval_time = intervals.get(last_char)
        time = time[: -1]

    return interval_time * int(time)


def get_date_time():
    # Import datetime module
    from datetime import datetime

    # Get current's date and time
    now = datetime.now()

    # Parse now's date to: Month Day Year
    month = now.strftime("%B")
    day = now.strftime("%d")
    year = now.strftime("%Y")

    # Parse time from gmtime()

    # Get current time
    time = gmtime()

    hours = strftime('%H', time)
    minutes = strftime('%M')
    seconds = strftime('%S')

    milliseconds = datetime.timestamp(now)

    return month, day, year, hours, minutes, seconds, milliseconds
