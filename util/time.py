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
    if last_char.isnumeric():
        time = time[: -1]

    return intervals.get(last_char) * int(time)
