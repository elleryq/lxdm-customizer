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
from lxdm_customizer_lib.ui_customizer import Ui_MainWindow
from lxdm_customizer_lib.lxdmconfig import LXDMConfig
from lxdm_customizer_lib.source import *
from lxdm_customizer_lib.util import isDisplayManagerLXDM


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if not isDisplayManagerLXDM():
            QMessageBox.information(None, "LXDM-customizer",
                "LXDM is not installed.  LXDM-customizer won't work.")
            sys.exit(-1)
        self.config = LXDMConfig()

        self.bindModels()
        self.bindEvents()

    def bindEvents(self):
        self.ui.actionE_xit.triggered.connect(self.close)
        self.ui.action_About.triggered.connect(self.showAbout)
        self.ui.buttonBrowse.clicked.connect(self.browseBackground)
        self.ui.action_Save.triggered.connect(self.save)

    def showAbout(self):
        QMessageBox.about(self, "LXDM Customizer",
                          "LXDM Customizer is a tool for customizer LXDM.")

    def save(self):
        if self.ui.checkNumlock.checkState() == Qt.CheckState.Checked:
            self.config.set('base', 'numlock', "1")
        else:
            self.config.set('base', 'numlock', "0")

        if self.ui.checkShowBottomPanel.checkState() == Qt.CheckState.Checked:
            self.config.set('display', 'bottom_pane', "1")
        else:
            self.config.set('display', 'bottom_pane', "0")

        if self.ui.checkShowLanguageSelector.checkState() == Qt.CheckState.Checked:
            self.config.set('display', 'lang', '1')
        else:
            self.config.set('display', 'lang', '0')

        if self.ui.checkShowKeyboard.checkState() == Qt.CheckState.Checked:
            self.config.set('display', 'keyboard', '1')
        else:
            self.config.set('display', 'keyboard', '0')

        greeters = findGreeters()
        self.config.set('base', 'greeter',
                        greeters[self.ui.comboGreeter.currentIndex()][1])

        gtkThemes = findGtkThemes()
        self.config.set('display', 'gtk_theme',
                        gtkThemes[self.ui.comboGtkTheme.currentIndex()][0])

        themes = findLXDMThemes()
        self.config.set('display', 'theme',
                        themes[self.ui.comboTheme.currentIndex()][0])

        if self.ui.editBackground.text():
            self.config.set('display', 'bg', self.ui.editBackground.text())

        # saveAs() is for testing.
        # self.config.saveAs("./lxdm.conf")
        self.config.save()

    def browseBackground(self):
        result = QFileDialog.getOpenFileName(self,
           "Select image file as background",
           "/usr/share/backgrounds",
           "Image files (*.png *.jpg *.jpeg)")
        fn, t = result
        if fn:
            self.ui.editBackground.setText(fn)
            self._setGraphicsViewImage(fn)

    def show(self):
        super(MainWindow, self).show()
        # Need to invoke fitInView here or the picture is small.
        self.ui.graphicsView.fitInView(self.ui.graphicsView.geometry(),
                                       Qt.KeepAspectRatio)

    def tryGetConfigInt(section, option):
        try:
            return self.config.getint(section, option)
        except:
            return None

    def createModel(self):
        model = QStandardItemModel(10, 1)
        model.setItem(0, 0, QStandardItem(tryGetConfigInt('base', 'numlock')))
        # TODO

    def bindModels(self):
        try:
            if self.config.getint('base', 'numlock') == 1:
                self.ui.checkNumlock.setCheckState(Qt.CheckState.Checked)
        except:
            pass

        try:
            if self.config.getint('display', 'bottom_pane') == 1:
                self.ui.checkShowBottomPanel.setCheckState(Qt.CheckState.Checked)
        except:
            pass

        try:
            if self.config.getint('display', 'lang') == 1:
                self.ui.checkShowLanguageSelector.setCheckState(Qt.CheckState.Checked)
        except:
            pass

        try:
            if self.config.getint('display', 'keyboard') == 1:
                self.ui.checkShowKeyboard.setCheckState(Qt.CheckState.Checked)
        except:
            pass

        try:
            background = self.config.get('display', 'bg')
            self.ui.editBackground.setText(background)
            if os.path.exists(background):
                self._setGraphicsViewImage(background)
        except Exception, ex:
            print(ex)

        greeters = findGreeters()
        self.ui.comboGreeter.setModel(self._createStandardItemModel(greeters))
        try:
            self.ui.comboGreeter.setCurrentIndex(self._findCurrentIndex(greeters,
                1, self.config.get('base', 'greeter')))
        except Exception, ex:
            print(ex)

        gtkThemes = findGtkThemes()
        self.ui.comboGtkTheme.setModel(self._createStandardItemModel(gtkThemes))
        try:
            self.ui.comboGtkTheme.setCurrentIndex(self._findCurrentIndex(gtkThemes,
                0, self.config.get('display', 'gtk_theme')))
        except Exception, ex:
            print(ex)

        themes = findLXDMThemes()
        self.ui.comboTheme.setModel(self._createStandardItemModel(themes))
        try:
            self.ui.comboTheme.setCurrentIndex(self._findCurrentIndex(themes,
                0, self.config.get('display', 'theme')))
        except Exception, ex:
            print(ex)

    def _setGraphicsViewImage(self, imagePath):
        self.ui.scene = QGraphicsScene(self.ui.graphicsView)
        self.ui.bg = self.ui.scene.addPixmap(QPixmap(imagePath))
        self.ui.graphicsView.setScene(self.ui.scene)
        self.ui.graphicsView.fitInView(self.ui.bg, Qt.KeepAspectRatio)
        self.ui.graphicsView.show()

    def _findCurrentIndex(self, data, x, value):
        for i, t in enumerate(data):
            if t[x] == value:
                return i
        return -1

    def _createStandardItemModel(self, data):
        model = QStandardItemModel(len(data), 1)
        for i, d in enumerate(data):
            item = QStandardItem(d[0])
            model.setItem(i, 0, item)
        return model


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
