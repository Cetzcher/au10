from urllib.parse import quote
import requests

class Networker:

    @staticmethod
    def make_request(host, port, sstr):
        """
        Makes  a REST request to a server at host:port
        :param host: host as str
        :param port: port as str
        :param sstr: the searchtex
        :return: a tuple of lang, prob, relieable, iso.
        """
        host, port = host, port
        qstr = quote(sstr)
        r = requests.get("http://{0}:{1}".format(host, port), params={"q": qstr})
        json = r.json()

        lang, prob, relieable, iso = json["lang"], json["prob"], json["reliable"], json["iso_code"]
        return lang, prob, relieable, iso