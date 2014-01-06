#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LXDM customizer"""

import sys
import os
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    print(QObject.tr("You need to install PySide."))
from lxdm_customizer_lib.ui_customizer import Ui_MainWindow
from lxdm_customizer_lib.lxdmconfig import LXDMConfig
from lxdm_customizer_lib.source import *
from lxdm_customizer_lib.util import isDisplayManagerLXDM


class MainWindow(QMainWindow):
    title = "LXDM-customizer"

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.isDirty = False
        self.ui.setupUi(self)

        if not isDisplayManagerLXDM():
            QMessageBox.information(None, self.title,
                self.tr("LXDM is not installed.  LXDM-customizer won't work."))
            sys.exit(-1)
        self.config = LXDMConfig()

        self.bindModels()
        self.bindEvents()

    def bindEvents(self):
        self.ui.actionE_xit.triggered.connect(self.onClose)
        self.ui.action_About.triggered.connect(self.showAbout)
        self.ui.buttonBrowse.clicked.connect(self.browseBackground)
        self.ui.action_Save.triggered.connect(self.onSave)
        
        checkboxs = [self.ui.checkNumlock,
                self.ui.checkShowBottomPanel,
                self.ui.checkShowLanguageSelector,
                self.ui.checkShowKeyboard]
        for checkbox in checkboxs:
            checkbox.stateChanged.connect(self.onCheckboxStateChanged)

        comboboxs = [self.ui.comboGreeter,
                self.ui.comboGtkTheme,
                self.ui.comboTheme]
        for combobox in comboboxs:
            combobox.currentIndexChanged.connect(self.onComboboxChanged)

        self.ui.editBackground.textChanged.connect(self.onLineEditChanged)
        self.ui.action_Save.setEnabled(False)

    def showAbout(self):
        QMessageBox.about(self, self.title,
            self.tr("LXDM Customizer is a tool for customizer LXDM."))

    def onSave(self):
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
        self.isDirty = False

    def browseBackground(self):
        result = QFileDialog.getOpenFileName(self,
           self.tr("Select image file as background"),
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

    def tryGetConfigInt(self, section, option):
        try:
            return self.config.getint(section, option)
        except:
            return 0

    def tryGetConfigString(self, section, option):
        try:
            return self.config.get(section, option)
        except:
            return ""

    def bindModels(self):
        self.ui.checkNumlock.setChecked(self.tryGetConfigInt('base',
                'numlock') == 1)
        self.ui.checkShowBottomPanel.setChecked(self.tryGetConfigInt('display',
                'bottom_pane') == 1)
        self.ui.checkShowLanguageSelector.setChecked(self.tryGetConfigInt('display',
                'lang') == 1)
        self.ui.checkShowKeyboard.setChecked(self.tryGetConfigInt('display',
                'keyboard') == 1)

        background = self.tryGetConfigString('display', 'bg')
        if background:
            self.ui.editBackground.setText(background)
            if os.path.exists(background):
                self._setGraphicsViewImage(background)

        greeters = findGreeters()
        self.ui.comboGreeter.setModel(self._createStandardItemModel(greeters))
        greeter = self.tryGetConfigString('base', 'greeter')
        self.ui.comboGreeter.setCurrentIndex(self._findCurrentIndex(greeters,
            1, greeter))

        gtkThemes = findGtkThemes()
        self.ui.comboGtkTheme.setModel(self._createStandardItemModel(
            gtkThemes))
        gtkTheme = self.tryGetConfigString('display', 'gtk_theme')
        self.ui.comboGtkTheme.setCurrentIndex(self._findCurrentIndex(gtkThemes,
            0, gtkTheme))

        themes = findLXDMThemes()
        self.ui.comboTheme.setModel(self._createStandardItemModel(themes))
        theme = self.tryGetConfigString('display', 'theme')
        self.ui.comboTheme.setCurrentIndex(self._findCurrentIndex(themes,
            0, theme))

    def makeActionSaveEnabled(self):
        self.ui.action_Save.setEnabled(True)

    def onCheckboxStateChanged(self, state):
        print("New state={0}".format(state))
        self.isDirty = True
        self.makeActionSaveEnabled()

    def onComboboxChanged(self, index):
        print("New index={0}".format(index))
        self.isDirty = True
        self.makeActionSaveEnabled()

    def onLineEditChanged(self, text):
        print("New text={0}".format(text))
        self.isDirty = True
        self.makeActionSaveEnabled()

    def onClose(self):
        if self.isDirty:
            button = QMessageBox.question(self, self.title,
                self.tr("You had changed settings, are you sure to exit?"),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.NoButton)
            if not button == QMessageBox.Yes:
                return
        self.close()

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
    translator = QTranslator()
    translation_path = os.path.join(sys.prefix, 'share', 'lxdm-customizer',
                                    'translations')
    if translator.load(QLocale.system(), "", "", translation_path):
        pass
    elif translator.load(QLocale.system(), "", "", "i18n"):
        pass
    app = QApplication(sys.argv)
    app.installTranslator(translator)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
