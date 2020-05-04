#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os
from logging import handlers

logger_name = "logger"
logger_level = logging.DEBUG
logger_tofile = True
logger_filepath = "./log/logger.log"


def New():
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    # format
    logger_format = logging.Formatter("[%(asctime)s.%(msecs)03d][%(level)s] %(pathname)s:%(lineno)d(%(funcName)s) ==> %(message)s", "%Y-%m-%d %H:%M:%S")

    # Filter
    logger.addFilter(Context())

    # console handler
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logger_level)
    handler_console.setFormatter(logger_format)
    logger.addHandler(handler_console)

    # file handler
    if logger_tofile:
        try:
            # mkdir logger dir
            try:
                os.makedirs(os.path.dirname(os.path.abspath(logger_filepath)))
            except FileExistsError as error:
                pass

            handler_file = logging.handlers.TimedRotatingFileHandler(filename=logger_filepath, when="D", encoding="utf-8", backupCount=7)
            handler_file.setLevel(logger_level)
            handler_file.setFormatter(logger_format)
            logger.addHandler(handler_file)
        except FileNotFoundError as error:
            print(error)
        except OSError as error:
            print(error)

    return logger


class Context(logging.Filter):
    def __init__(self):
        self.level = {10: "DBG", 20: "INF", 30: "WRN", 40: "ERR", 50: "CRT"}

    def filter(self, record):
        if record.levelno in self.level:
            record.level = self.level[record.levelno]
            return True
