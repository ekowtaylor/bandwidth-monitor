# Represents the measure results
class MeasureResult:
    def __init__(self, source: str):
        self.source = source

        self.connection_available = -1
        self.connection_type = "None"
        self.ping_rate: int = -1.0
        self.download_rate: float = 0.0
        self.upload_rate: float = 0.0
        self.month = 0
        self.day = 0
        self.year = 0
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        self.timestamp = 0

    def parse_rates(self):
        if self.source == 'speedtest.net':
            self.download_rate /= 1000000
            self.upload_rate /= 1000000
        elif self.source == 'fast.com':
            self.download_rate = self.download_rate
            self.upload_rate = self.upload_rate


    def get_date(self):
        return f'{self.hour}:{self.minutes}:{self.seconds}'


    def get_time(self) -> str:
        return f'{self.hour}:{self.minutes}:{self.seconds}'


    def print(self):
        print()

        date = self.get_date()
        time = self.get_time()

        print(f'[Measure Result]: Source: {self.source}, Date: {date}, Time: {time}, Timestamp: {self.timestamp}')

        print(f'\tConnection Available: {self.connection_available}, Connection Type: {self.connection_type}, '
              f'Ping Rate: {self.ping_rate}, Download Rate: {self.download_rate} mb/s, '
              f'Upload Rate: {self.upload_rate} mb/s')
