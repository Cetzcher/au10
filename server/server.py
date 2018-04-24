#!/usr/bin/python3

import cherrypy
import argparse
import json

from urllib.parse import unquote

import math
from langdetect import detect_langs
from iso639 import to_name
# the suggested library does not compile this provides tho this provides the same functionality

RELIABILITY_THRESHOLD = 0.80

class Service(object):

    @cherrypy.expose
    def index(self, q):
        """
        root address of the server.
        q is the search string that should be analyzed.
        for example server/?q=hello%20World would search for hello world.

        :param q: the GET query param to be used
        :return: a respones
        """
        # take the query from url encoded format to a string
        qstr = unquote(q)
        langs = detect_langs(qstr)
        best = langs[0]
        prob, iso_code = best.prob, best.lang
        is_relieable = prob >= RELIABILITY_THRESHOLD
        language_name = to_name(iso_code)
        shortend_query = qstr[0: min(len(qstr), 16)] # send back the first 32 characters.
        return json.dumps({"query_short": shortend_query,
                           "prob": math.floor(prob * 100),
                           "reliable": is_relieable,
                           "iso_code": iso_code,
                           "lang": language_name}) + "\n"


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

    args = parser.parse_args()
    port = args.port[0]
    host = args.host[0]
    print("running on", host, ":", port)
    cherrypy.config.update({'server.socket_port': port})
    cherrypy.config.update({'server.socket_host': host})
    cherrypy.quickstart(Service())
