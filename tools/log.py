# -*- coding:utf-8 -*-
# 记录文件

import sys
import utils
import logging
import ConfigParser

class Config(object):
    '''read config file and parse it'''
    def __init__(self, filename):
        object.__init__(self)
        
        self.optimizer_ui_path = ""
        self.optimizer_ui_folder = ""
        self.image_scale = None
        self.alpha_threshold = None

        self.filename = filename
        self.__read_config(filename)



    def __read_config(self, filename):
        try:
            self._record_config = ConfigParser.ConfigParser()
            self._record_config.read(filename)

            self._config_dic = {}
            self._config_dic["path"] = {}
            path_items = self._record_config.items("path")
            for i in range(0,len(path_items),1):
                tmp_one_item = path_items[i]
                self._config_dic["path"][tmp_one_item[0]] = tmp_one_item[1]

            
            self._config_dic["option"] = {}
            option_items = self._record_config.items("option")
            for i in range(0,len(option_items),1):
                tmp_one_item = option_items[i]
                self._config_dic["option"][tmp_one_item[0]] = tmp_one_item[1]

            self.is_init = True
        except Exception as e:
            self.is_init = False
            print "read ini fail", e
    
    def getRecordValueByKey(self, section_key, option_key):
        if not self._config_dic.has_key(section_key):
            return ""
        
        option_dic = self._config_dic[section_key]

        if not option_dic.has_key(option_key):
            return ""

        return option_dic[option_key]

    def update_config(self, section_dict):
        config = ConfigParser.ConfigParser()
        config.read(self.filename)
        for section, items in section_dict.items():
            if not config.has_section(section):
                config.add_section(section)
            for k, v in items.items():
                config.set(section, k, v)
            
        config.write(open(self.filename, "w+"))


class CustomLog(object):
    '''handle custom log info'''
    def __init__(self):
        object.__init__(self)
        self._util_obj = utils.Utils()
        self.__init_logging__()

    def init_widget(self, widget):
        self.__display = widget

    def append_log(self, log):
        logging.info('log')
        self.__display.append_log(log)

    def write(self, error):
        self.__display.append_log(error)

    def __init_logging__(self):
        self._util_obj.create_dir_not_exist("./log")
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename='./log/logDebug.txt', level=logging.INFO, format=LOG_FORMAT)
