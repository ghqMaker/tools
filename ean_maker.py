# -*- coding:utf-8 -*-
#压缩纹理

import sys
import os
# import subprocess
# import shutil
# from xml.etree.ElementTree import ElementTree
from PyQt4 import QtGui, QtCore
# import data_parser
# import log
# from utils import *
# from base import *
from common import *
from make_ean import *
from utils import *
from base_widget import *
import unicodedata
# import json
# import biplist
# import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

SOURCE_OUTPUT_PATH_KEY = "ean_output_path"


_outPutPath = os.path.abspath('.') + "\picture"


class EanMaker(BaseWidget):

    def __init__(self, parent=None):
        BaseWidget.__init__(self, parent)
        self.__obj_utils = utils.Utils()

        self.__init_data__()
        self.__init_child()
        self.__init_layout()
        self.__init_event()
        self.__init_folder()
        #test image
        # utils.extract_pixel("E:/sealsky/doc/res/技术调用/3单元/20016/stat_20000.png")

    def __init_data__(self):
        pass
        #self.print_box_list = {"200":(708,472),"300":}

    def __init_folder(self):
        self.__obj_utils.create_dir_not_exist(
            self.__obj_utils.transform_path(_outPutPath.replace("\\", "/")))


    def __init_child(self):

        __int_validator = QtGui.QIntValidator(0, 99999999)

        self.__image_title_label = QtGui.QLabel("产品名称：")
        self.__image_title_edit = QtGui.QLineEdit()
       # self.__image_button = QtGui.QPushButton("打开")

        # self.__is_root_cb = QtGui.QCheckBox("根目录")
        # self.__is_root_cb.setVisible(False)

        self.__target_ean_code_label = QtGui.QLabel("条形码")
        self.__target_ean_code_edit = QtGui.QLineEdit()
        #self.__target_button = QtGui.QPushButton("打开")

        self.__target_num_label = QtGui.QLabel("贴标数量")
        self.__target_num_edit = QtGui.QLineEdit()

        self.__target_info_label = QtGui.QLabel("产品信息")
        self.__target_info_edit = QtGui.QLineEdit()

        self.__target_path_label = QtGui.QLabel("生成路径")
        self.__image_path_edit = QtGui.QLineEdit()
        self.__image_path_button = QtGui.QPushButton("打开")

        self.__target_len_label = QtGui.QLabel("长(mm)")
        self.__target_len_edit = QtGui.QLineEdit()

        self.__target_width_label = QtGui.QLabel("宽(mm)")
        self.__target_width_edit = QtGui.QLineEdit()

        self.__target_print_label = QtGui.QLabel("打印像素")
        self.__target_print_edit = QtGui.QLineEdit()
        # self.__target_print_Box = QtGui.QComboBox(self)

        # self.__target_print_Box.addItem("200")
        # self.__target_print_Box.addItem("300")
        # self.__target_print_Box.addItem("500")

        self.__confirm_button = QtGui.QPushButton("生成")
        self.__makeEan = makeEan()

    def __init_layout(self):

        self._grid.addWidget(self.__image_title_label, 0, 0)
        self._grid.addWidget(self.__image_title_edit, 0, 1)
        #self._grid.addWidget(self.__image_button, 0, 2)
        # self._grid.addWidget(self.__is_root_cb, 0, 3)
        self._grid.addWidget(self.__target_num_label, 0, 3)
        self._grid.addWidget(self.__target_num_edit, 0, 4)

        self._grid.addWidget(self.__target_ean_code_label, 1, 0)
        self._grid.addWidget(self.__target_ean_code_edit, 1, 1)

        self._grid.addWidget(self.__target_info_label, 1, 3)
        self._grid.addWidget(self.__target_info_edit, 1, 4)
        #self._grid.addWidget(self.__target_button, 1, 2)

        self._grid.addWidget(self.__target_len_label, 2, 3)
        self._grid.addWidget(self.__target_len_edit, 2, 4)

        self._grid.addWidget(self.__target_width_label, 3, 3)
        self._grid.addWidget(self.__target_width_edit, 3, 4)

        self._grid.addWidget(self.__target_path_label, 2, 0)
        self._grid.addWidget(self.__image_path_edit, 2, 1)
        self._grid.addWidget(self.__image_path_button, 2, 2)

        self._grid.addWidget(self.__target_print_label, 3, 0)
        self._grid.addWidget(self.__target_print_edit, 3, 1)

        self._grid.addWidget(self.__confirm_button, 4, 4)

        self.setLayout(self._grid)
        self.__init_show__()

    def __init_show__(self):
        is_has_record_path = True
        if not (self._config.is_init and len(self._config.getRecordValueByKey("path", SOURCE_OUTPUT_PATH_KEY)) > 0):
            self.__image_path_edit.setText(
                self.__obj_utils.transform_path(_outPutPath))
            is_has_record_path = False
        if is_has_record_path:
            self.__image_path_edit.setText(
                self._config.getRecordValueByKey("path", SOURCE_OUTPUT_PATH_KEY))
        self._output_path = str(self.__image_path_edit.text()).decode("utf-8")

        self.__target_len_edit.setText(IMG_DEFAULT_LEN)
        self.__target_width_edit.setText(IMG_DEFAULT_WIDTH)
        self.__target_print_edit.setText(PRINT_DEFAULT_DIP)

    def __init_event(self):
        self.connect(
            self.__confirm_button,
            QtCore.SIGNAL("clicked()"),
            self.__on_make_ean
        )

        self.connect(
            self.__image_path_button,
            QtCore.SIGNAL("clicked()"),
            self.__on_open_image
        )

    def __on_open_image(self):
        dir_name = QtGui.QFileDialog.getExistingDirectory(
            self,
            "Open Director", self.__image_path_edit.text(),
            QtGui.QFileDialog.ShowDirsOnly
        )
        if dir_name.isEmpty():
            return

        self.__image_path_edit.setText(dir_name)
        self._output_path = str(self.__image_path_edit.text()).decode("utf-8")
       # _outPutPath = _outPutPath.encode(encoding='UTF-8',errors='strict')

    def __on_make_ean(self):
       #     print(str(self.__target_ean_code_label.text()).decode("utf-8"))
        self._title_txt = "AAA" or str(self.__image_title_edit.text())
        self._info_txt = "AAA" or str(self.__target_info_edit.text())
        self._ean_code = 'AAAAAAAAAA' or ''.join(
            str(self.__target_ean_code_edit.text()).split())
        self._num = '3' or str(self.__target_num_edit.text())
        self._size = (str(self.__target_len_edit.text()),str(self.__target_width_edit.text()))
        self._print_dip = int(self.__target_print_edit.text())
        if self.__checkInput():
            result = self.__makeEan.createEan(self._title_txt, self._info_txt, self._ean_code, self._num, self._output_path, self._size, self._print_dip)
            if result:
                self.__on_console_text("success！！！path：" + self._output_path)

    def __checkInput(self):

        def _check_num(num, txt):
            if len(num) <= 0:
                self.__on_console_text("fail!，请填入“" + txt + "”")
                return False
            elif not self.__obj_utils.is_number(num) or int(num) < 1:
                self.__on_console_text("fail!，"+ txt +"必须为 > 1 整数")
                return False
            # elif int(num) <= 0:
            #     self.__on_console_text("fail!，"+ txt +"得大于“1”")
            #     return False
            return True

        if len(self._title_txt) <= 0:
            self.__on_console_text("fail!，请填入“产品名称”")
            return False

        if not _check_num(self._num,"数量"):
            return False

        if not _check_num(self._num,"打印像素"):
            return False
        flag = False
        if not(0 < len(self._ean_code) < 11):
            self.__on_console_text("fail!，“条形码”长度为10！")
            return flag
        for ch in self._ean_code:
            if not (64 < ord(ch) < 91 or 47 < ord(ch) < 58):
                flag = True
                break
        if flag:
            self.__on_console_text("fail!，“条形码”只能输入：数字、大写字母")
            return False

        if len(self._info_txt) <= 0:
            self.__on_console_text("fail!，请填入“产品信息”")
            return False
        def _check_size(num, txt):
            if len(num) <= 0:
                    self.__on_console_text("fail!，请填入“" + txt + "”")
                    return False
            elif not self.__obj_utils.is_number(num) or float(num) < 1:
                    self.__on_console_text("fail!，"+ txt +"必须为 > 1 ")
                    return False
            return True
        if not _check_size(self._size[0],"长度"):
            return False
        if not _check_size(self._size[1],"宽度"):
            return False

        return True

    def __on_console_text(self, text):
        Common.custom_log.append_log(text)

    def close(self):
        sec = {}
        sec["path"] = {}
        sec["path"][SOURCE_OUTPUT_PATH_KEY] = self.__image_path_edit.text()

        self._config.update_config(sec)
