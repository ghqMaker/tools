# -*- coding:utf-8 -*-
# 工具类，可供任何地方调用

import sys
import os
# import subprocess
# import shutil
# from xml.etree.ElementTree import ElementTree
# from PyQt4 import QtGui, QtCore
# import log
# import json
# import biplist
# import struct
# import hashlib
# import copy
# import re
# import openpyxl
# # from openpyxl.cell import get_column_letter
# import xlrd
# import shutil
# import time

TEXTURE_FORMAT_PNG = "png"
TEXTURE_FORMAT_JPG = "jpg"
TEXTURE_FORMAT_PVRCCZ = "pvr.ccz"
I18N_FLAG = "i18n"

class Utils(object):
    def __init__(self):
        super(Utils, self).__init__()
       
    def create_dir_not_exist(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def is_number(self, s):
        try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
            float(s)
            return True
        except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
            pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
        try:
            import unicodedata  # 处理ASCii码的包
            unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
            return True
        except (TypeError, ValueError):
            pass
        return False

    def transform_path(self, path):
        return path.replace("\\","/")