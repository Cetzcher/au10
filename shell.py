import argparse
import os
import sys

sys.path.insert(0, os.path.abspath('../'))
from au10.networker import Networker


if __name__ == '__main__':
    # setup an argument parser to read a port from the command line.
    # usage: python3 server -p PORT or ./server -p PORT
    parser = argparse.ArgumentParser(description='start cherrypy webservice')
    parser.add_argument(
        '-p', '--port', type=int, help='Port number',
        default=[8099], required=False, nargs='+')
    parser.add_argument(
        '-H', '--host', type=str, help='Host, leave blank for 127.0.0.1',
        default=["127.0.0.1"], required=False, nargs='+')
    parser.add_argument(
        '-s', '--search', type=str, help='string, leave blank for empty string',
        default=[""], required=False, nargs='+')

    args = parser.parse_args()
    port = args.port[0]
    host = args.host[0]
    s = args.search[0]
    print(*Networker.make_request(host, port, s))