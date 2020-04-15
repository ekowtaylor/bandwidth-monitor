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
