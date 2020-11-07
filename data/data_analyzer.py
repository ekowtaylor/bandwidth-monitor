from storage import storage_manager


def get_summary(time_started, debug=False):
    query = storage_manager.query(
        "select count(download_rate) as amount, avg(download_rate) as download_rate_avg, avg(upload_rate) as "
        "upload_rate_avg from bandwidth_data "
        f'where connection_available = 1 and time_timestamp >= {time_started};')

    upload_rate_avg = query[0][2]
    download_rate_avg = query[0][1]
    if len(query) < 1 or download_rate_avg is None or upload_rate_avg is None:
        if debug:
            print('[INFO]: No new traffic measured.')

        return 0, 0, 0

    requests = query[0][0]
    if debug:
        print(
            f'[INFO]: Summary of operation: \n\tAmount of requests: {requests}, '
            f'Download Rate Average: {download_rate_avg}, Upload Rate Average: {upload_rate_avg}'
        )
    return requests, download_rate_avg, upload_rate_avg


def get_data(query: str) -> list:
    storage_manager.close_database()

    return storage_manager.query(query)
