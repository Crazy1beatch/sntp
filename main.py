import argparse

import server


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '-delay', dest="delay", type=int, help="Delay of returning time", default=0)
    parser.add_argument('-p', '-port', dest="port", type=int, help="listening port", default=123)
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    host = '127.0.0.1'
    server.run_server(host, args.port, args.delay)


if __name__ == '__main__':
    main()
