# -*- coding:utf-8 -*-
# 主入口文件

import sys
import os
from PyQt4 import QtGui, QtCore

import main_window
# from common import Common

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

def __get_center_pos(w, h):
    screen = QtGui.QDesktopWidget().screenGeometry()
    return (screen.width() - w) * 0.5, (screen.height() - h) * 0.5

def main():

    os.chdir(os.getcwd())

    reload(sys)
   # sys.setdefaultencoding("utf-8")

    codec = QtCore.QTextCodec.codecForName("utf-8")
    QtCore.QTextCodec.setCodecForLocale(codec)
    QtCore.QTextCodec.setCodecForCStrings(codec)
    QtCore.QTextCodec.setCodecForTr(codec)

    app = QtGui.QApplication(sys.argv)
    ct_widget = main_window.MainWindow()
    ct_widget.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
    ct_widget.show()
    x, y = __get_center_pos(
        ct_widget.frameSize().width(), 
        ct_widget.frameSize().height()
    )
    ct_widget.move(x, y)

    #sys.stderr = Common.customog

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()