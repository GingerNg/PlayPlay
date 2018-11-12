# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: playplay_config.py
@time: 2018/5/4 23:33
"""
import configparser
import os

from utils.logger_utils import get_logging,init_logging

init_logging()
logger = get_logging(__name__)

CONF_FILE = "playplay.conf"
if not os.path.isfile(CONF_FILE):
    logger.error("config file path is wrong")
cf = configparser.ConfigParser()

cf.read(CONF_FILE)
sections = cf.sections()


mongo_url = cf.get("mongo","url")
spider_coll = cf.get("mongo","spider_coll")

gather_db = cf.get("mongo","gather_db")
gather_coll = cf.get("mongo","gather_coll")


# print(plugin_path)
