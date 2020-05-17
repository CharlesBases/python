#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import time

import requests


def get(url, params):
    try:
        infor = __information()

        response = requests.get(url, params, allow_redirects=False)
        response.raise_for_status()

    except requests.HTTPError as error:
        print(error)
    finally:
        print(infor.logger(response.status_code, "GET", response.url))
        pass


def post(url, json):
    try:
        infor = __information()

        response = requests.post(url, json, allow_redirects=False)
        response.raise_for_status()

    except requests.HTTPError as error:
        print(error)
    finally:
        print(infor.logger(response.status_code, "POST", response.url))
        pass


class __information(object):
    def __init__(self):
        self.start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.start_timens = time.time_ns()

    def logger(self, status, method, path):
        return "%s | %d | %s | %s %s" % (self.start, status, ("%.3fs" % ((time.time_ns() - self.start_timens) / 1e9), method, path))
