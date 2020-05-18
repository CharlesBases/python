#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time, datetime
import unittest

from utils import logger, request


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
        request.get("http://www.baidu.com")
