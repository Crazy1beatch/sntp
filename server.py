import socket
from multiprocessing.pool import ThreadPool

import sntp_package


def answer_to_client(sock, address, data, delay):
    answer = sntp_package.get_new_package(data, sntp_package.get_bytes(delay), delay)
    sock.sendto(answer + sntp_package.get_bytes(delay), address)


def run_server(host, port, delay):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print("Server is running!")
        while True:
            data, address = sock.recvfrom(1024)
            print(f'\t{address[0]}:{address[1]} connected to {host}:{port}')
            ThreadPool(10).apply_async(answer_to_client, args=(sock, address, data, delay))
