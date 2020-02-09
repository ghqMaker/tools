#-*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore, Qt

# from base import *
# from common import *

class BaseWidget(QtGui.QWidget):
    '''base widget'''
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

      #  self._data_parser = Common.data_parser
     #   self._config = Common.config
        
        self._init_child()

    def _init_child(self):
        self._grid = QtGui.QGridLayout()
        self._grid.setSpacing(20)
        self.setLayout(self._grid)
        pass