import pyspeedtest


class MeasureResult:
    def __init__(self, download_rate, upload_rate, ping):
        self.download_rate = download_rate
        self.upload_rate = upload_rate
        self.ping = ping


def get_speedtest_result() -> MeasureResult:
    speedtest = pyspeedtest.SpeedTest()
    download_rate = speedtest.download()
    upload_rate = speedtest.upload()
    ping = speedtest.ping()

    return MeasureResult(download_rate=download_rate, upload_rate=upload_rate, ping=ping)


if __name__ == '__main__':
    print('_______________________________________')
    print()
    print('Author: Eyal Berkovich')
    print('Description: Small Python script for measuring ')
