import socket


# noinspection PyBroadException
def is_internet_available(hostname: str) -> bool:
    try:
        # try resolve hostname
        host = socket.gethostbyname(hostname)
        sock = socket.create_connection((host, 80), 2)
        sock.close()

        return True
    except:
        pass

    return False


# TODO: Implement get_connection_type() function
def get_connection_type() -> str:
    return "Not implemented yet"
