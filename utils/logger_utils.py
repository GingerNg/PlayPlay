# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: logger_utils.py
@time: 2018/4/26 17:21
"""

import logging.config
import os
import logging

from utils.constants import CONF_PATH

def init_logging():
    logging.config.fileConfig(os.path.join(CONF_PATH,"log.conf"))
    return logging.getLogger("logger_algo")


def getLogging_file():
    logging.config.fileConfig(os.path.join(CONF_PATH,"log.conf"))
    return logging.getLogger("logger_file")

def get_logging(name = __name__):
    logger = logging.getLogger(name=name)
    return logger


if __name__=="__main__":
    logger = init_logging()
    logger.info("this is an example!")

