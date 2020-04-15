import sqlite3

from measure.measure_result import MeasureResult


def connect():
    global conn

    print('[INFO]: Connecting to database: bandwidth-monitor.db')
    conn = sqlite3.connect('bandwidth-monitor.db')

    '''
        self.connection_available = connection_available
        self.connection_type = connection_type
        self.ping_rate = ping_rate
        self.download_rate = download_rate
        self.upload_rate = upload_rate
        self.date = date
        self.time = time
        self.source = source
    '''

    conn.execute("""create table if not exists bandwidth_data (
                 data_source varchar(9) not null,
                 connection_available boolean default 0,
                 connection_type varchar(8) default "none",
                 ping_rate int,
                 download_rate int,
                 upload_rate int,
                 date_month char(2),
                 date_day char(2),
                 date_year char(4),
                 time_hours char(2),
                 time_minutes char(2),
                 time_seconds char(2));
                 """)
    print('[INFO]: Connected to database: bandwidth-monitor.db')


def store_measure_result(measure_result: MeasureResult) -> None:
    global conn

    if conn is None:
        connect()

    connection_available = 0
    if measure_result.connection_available:
        connection_available = 1

    data = (
        measure_result.source,
        connection_available,
        measure_result.connection_type,
        measure_result.ping_rate,
        measure_result.download_rate,
        measure_result.upload_rate,
        measure_result.month,
        measure_result.day,
        measure_result.year,
        measure_result.hour,
        measure_result.minutes,
        measure_result.seconds
    )

    conn.executemany("""insert into bandwidth_data (
                     data_source,
                     connection_available,
                     connection_type,
                     ping_rate,
                     download_rate,
                     upload_rate,
                     date_month,
                     date_day,
                     date_year,
                     time_hours,
                     time_minutes,
                     time_seconds) 
                     VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
                     """,
                     (data,)
                     )

    conn.commit()
    conn.close()


def close_database():
    conn.close()


def cache_last_measure_result(measure_result: MeasureResult) -> None:
    pass
