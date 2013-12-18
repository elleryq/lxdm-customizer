#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LXDM customizer"""
from __future__ import print_function
import sys
import os
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    print("You need to install PySide.")
from ui_customizer import Ui_MainWindow
from lxdm_customizer_lib.lxdmconfig import LXDMConfig


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.config = LXDMConfig()

        self.bindModels()
        self.bindEvents()

    def bindEvents(self):
        self.ui.actionE_xit.triggered.connect(self.close)
        self.ui.action_About.triggered.connect(self.showAbout)

    def showAbout(self):
        QMessageBox.about(self, "LXDM Customizer",
                          "LXDM Customizer is a tool for customizer LXDM.")

    def bindModels(self):
        if self.config.getint('base', 'numlock')==1:
            self.ui.checkNumlock.setCheckState(Qt.CheckState.Checked)
        if self.config.getint('display', 'bottom_pane')==1:
            self.ui.checkShowBottomPanel.setCheckState(Qt.CheckState.Checked)
        if self.config.getint('display', 'lang')==1:
            self.ui.checkShowLanguageSelector.setCheckState(Qt.CheckState.Checked)
        if self.config.getint('display', 'keyboard')==1:
            self.ui.checkShowKeyboard.setCheckState(Qt.CheckState.Checked)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
