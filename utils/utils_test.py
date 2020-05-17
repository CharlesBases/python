#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time, datetime
import unittest

from utils import logger


class Test(unittest.TestCase):
    def test_logger(self):
        log = logger.New()

        log.debug("debug")
        log.info("info")
        log.warning("warning")
        log.error("error")
        log.critical("critical")

    def test_mysql(self):
        pass

    def test_request(self):
        start_timens = time.time_ns()
        start_date = datetime.datetime.now()
        print(time.mktime(time.strptime("%Y-%m-%d %H:%M:%S.%f", start_date)))
        time.sleep(1.5)
        print(time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime(start_timens / 1e9)))
