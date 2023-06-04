import datetime
import struct


def get_new_package(previous_package: bytes, receive_time: bytes, delay: int) -> bytes:
    return (
            struct.pack('!B', 28)
            + struct.pack('!B', 1)
            + struct.pack('!b', 0)
            + struct.pack('!b', -20)
            + struct.pack('!i', 0)
            + struct.pack('!i', 0)
            + struct.pack('!i', 0)
            + get_bytes(delay)
            + previous_package[40:48]
            + receive_time
    )


def get_bytes(delay: int) -> bytes:
    time = (datetime.datetime.utcnow() - datetime.datetime(1900, 1, 1)).total_seconds() + delay
    seconds, mil_seconds = [int(x) for x in str(time).split('.')]
    return struct.pack('!II', seconds, mil_seconds)
