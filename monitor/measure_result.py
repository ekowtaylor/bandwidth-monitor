# Represents the measure results
class MeasureResult:
    def __init__(self, ping_rate, download_rate, upload_rate, date, time, source: str):
        self.ping_rate = ping_rate
        self.download_rate = download_rate
        self.upload_rate = upload_rate
        self.date = date
        self.time = time
        self.source = source

    def print(self):
        print()

        print(f'Measure results: Source: {self.source}, Date: {self.date}, Time: {self.time}')

        if self.source == 'speedtest.net':
            print(f'\tPing Rate: {self.ping_rate} '
                  f'Download Rate: {self.download_rate / 1000000} mb/s, Upload Rate: {self.upload_rate / 1000000} mb/s')
        elif self.source == 'fast.com':
            print(f'\tPing Rate: {self.ping_rate} '
                  f'Download Rate: {self.download_rate / 1024} mb/s, Upload Rate: {self.upload_rate / 1024} mb/s')

        print()
