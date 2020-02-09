# -*- coding:utf-8 -*-
#主窗口

from PyQt4 import QtGui, QtCore
from common import *
# from utils import *
# from optimizer_ui import *
# from lua_ui import *
# from fashion_img import *
# from build_mobile_package import *
# from encrypt_texture import *
from ean_maker import *
# from effect import *
# from battle_unit import *
# from gen_data_ui import *
# from i18n_win import *
# from icon_copy import *
# from svn_ui import *
# from horse import *
# from live2d import *
# import log
# from build_as_android import *

reload(sys)
#sys.setdefaultencoding( "utf-8" )

class MainWindow(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Utils")
        self.setWindowIcon(QtGui.QIcon("icons/128.png"))

        self.__init_config()
        self.__init_child()

    def __init_config(self):
        Common.startup()

    def __init_child(self):

        self.__grid = QtGui.QGridLayout()
        self.__grid.setSpacing(50)
        self.setLayout(self.__grid)

        self.__hbox = QtGui.QHBoxLayout()
        self.__grid.addLayout(self.__hbox, 0, 0)

        self.__tab_bar = QtGui.QTabWidget()
        self.__hbox.addWidget(self.__tab_bar)

        self.__tab_bar.setCurrentIndex(0)

        self.__ean_maker= EanMaker()

        self.__tab_bar.addTab(self.__ean_maker, "生成条形码")
       

        # self.__i18n_tp.setIsForCehua(is_for_cehua)

        #self.__log_label = QtGui.QLabel("输出")
        self.__console_text = QtGui.QTextEdit()
        self.__clear_console_button = QtGui.QPushButton("清空输出")

        #self.__grid.addWidget(self.__log_label, 1, 0)
        self.__grid.addWidget(self.__clear_console_button, 1, 0)
        self.__grid.addWidget(self.__console_text, 2, 0)

        self.connect(
            self.__clear_console_button,
            QtCore.SIGNAL("clicked()"),
            self.__on_clear_log
        )

        Common.custom_log.init_widget(self)

    def append_log(self, text):
        self.__console_text.append(text)
        self.__console_text.repaint()

    def __on_clear_log(self):
        self.__console_text.clear()

    # 关闭时候执行
    def closeEvent(self, event):
        # self.__optimizer_ui.close()
        # # self.__fashion_img.close()
        # self.__buid_mob_pack.close()
        # self.__encrypt_texture.close()
        self.__ean_maker.close()
        # self.__effect.close()
        # self.__battle_unit.close()
        # self.__horse.close()
        # self.__gen_data_ui.close()
        # self.__i18n_tp.close()
        # self.__icon_copy.close()
        # self.__lua_ui.close()
        # self.__svn_ui.close()
        # self.__live2d_ui.close()
        # self.__buid_as_android.close()
        pass
