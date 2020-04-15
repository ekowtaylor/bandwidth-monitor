# Represents the measure results
class MeasureResult:
    def __init__(self, connection_available: bool, connection_type: str, ping_rate, download_rate,
                 upload_rate, month, day, year, hour, minutes, seconds, source: str):
        self.connection_available = connection_available
        self.connection_type = connection_type
        self.ping_rate = ping_rate
        self.download_rate = download_rate
        self.upload_rate = upload_rate
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.source = source

        self.parse_rates()

    def parse_rates(self):
        if self.source == 'speedtest.net':
            self.download_rate /= 1000000
            self.upload_rate /= 1000000
        elif self.source == 'fast.com':
            self.download_rate = self.download_rate
            self.upload_rate = self.upload_rate

    def print(self):
        print()

        date = f'{self.day}/{self.month}/{self.year}'
        time = f'{self.hour}:{self.minutes}:{self.seconds}'

        print(f'Measure results: Source: {self.source}, Date: {date}, Time: {time}')

        print(f'\tConnection Available: {self.connection_available}, Connection Type: {self.connection_type}, '
              f'Ping Rate: {self.ping_rate} Download Rate: {self.download_rate} mb/s, '
              f'Upload Rate: {self.upload_rate} mb/s')

        print()
