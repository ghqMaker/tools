#-*- coding:utf-8 -*-
#通用类

import log

CONFIG_FILE = "config.ini"

class Common(object):
    def __init__(self):
        object.__init__(self)

    @staticmethod
    def startup():
        Common.config = log.Config(CONFIG_FILE)
        Common.custom_log = log.CustomLog()
