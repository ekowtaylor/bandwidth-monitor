from storage import storage_manager


def print_summary(time_started):
    query = storage_manager.query(
        "select count(download_rate) as amount, avg(download_rate) as download_rate_avg, avg(upload_rate) as " \
        "upload_rate_avg from bandwidth_data " \
        f'where connection_available = 1 and time_timestamp >= {time_started};')

    print(f'[INFO]: Summary of operation: '
          f'\n\tAmount of probes: {query[0]}, Download Rate Average: {query[1]}, Upload Rate Average: {query[2]}')
