#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LXDM customizer"""
from __future__ import print_function
import sys
import os
try:
    from PySide.QtGui import *
except ImportError:
    print("You need to install PySide.")
from ui_customizer import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bindEvents()

    def bindEvents(self):
        self.ui.actionE_xit.triggered.connect(self.close)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
