import sqlite3

from measure.measure_result import MeasureResult

# TODO: Read value from config
DATABASE: str = 'bandwidth-monitor.db'


conn: sqlite3.Connection = None


def query(statement: str) -> list:
    global conn

    if conn is None:
        connect()

    cur = conn.cursor()
    cur.execute(statement)
    # cur.execute("select * from bandwidth_data")

    fetchall = cur.fetchall()

    return fetchall


def connect():
    global conn

    print(f'[INFO]: Connecting to database: {DATABASE}')

    if conn is not None:
        print(f'[INFO]: Already connected to database: {DATABASE}')
        return

    conn = sqlite3.connect(DATABASE)

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
                 time_seconds char(2),
                 time_timestamp integer);
                 """)

    print(f'[INFO]: Connected to database: {DATABASE}')


def store_measure_result(measure_result: MeasureResult) -> None:
    global conn

    if measure_result is None:
        return

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
        measure_result.seconds,
        measure_result.timestamp
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
                     time_seconds,
                     time_timestamp) 
                     VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);
                     """,
                     (data,)
                     )

    conn.commit()


def close_database() -> None:
    global conn

    if conn is not None:
        conn.close()
        conn = None


def cache_last_measure_result(measure_result: MeasureResult) -> None:
    pass
