#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time

import requests


def get(url, params=None):
    try:
        infor = __information()

        response = requests.get(url, params, allow_redirects=False)
        response.raise_for_status()
    except requests.HTTPError as error:
        print(error)
    finally:
        print(infor.logger(response.status_code, response.request.method, response.url))


def post(url, json):
    try:
        infor = __information()

        response = requests.post(url, json, allow_redirects=False)
        response.raise_for_status()

    except requests.HTTPError as error:
        print(error)
    finally:
        print(infor.logger(response.status_code, response.request.method, response.url))


class __information(object):
    def __init__(self):
        self.start_time = time.time()
        self.start = "%s.%03d" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(self.start_time))), (self.start_time - int(self.start_time)) * 1000)

    def logger(self, status, method, path):
        return "%s | %d | %s | %s %s" % (self.start, status, ("%.3fs" % (time.time() - self.start_time)), method, path)
