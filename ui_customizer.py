# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customizer.ui'
#
# Created: Wed Dec 18 16:59:46 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboGreeter = QtGui.QComboBox(self.tab)
        self.comboGreeter.setObjectName("comboGreeter")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboGreeter)
        self.checkNumlock = QtGui.QCheckBox(self.tab)
        self.checkNumlock.setObjectName("checkNumlock")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkNumlock)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboGtkTheme = QtGui.QComboBox(self.tab_2)
        self.comboGtkTheme.setObjectName("comboGtkTheme")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboGtkTheme)
        self.checkShowBottomPanel = QtGui.QCheckBox(self.tab_2)
        self.checkShowBottomPanel.setObjectName("checkShowBottomPanel")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkShowBottomPanel)
        self.checkShowLanguageSelector = QtGui.QCheckBox(self.tab_2)
        self.checkShowLanguageSelector.setObjectName("checkShowLanguageSelector")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkShowLanguageSelector)
        self.checkShowKeyboard = QtGui.QCheckBox(self.tab_2)
        self.checkShowKeyboard.setObjectName("checkShowKeyboard")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.checkShowKeyboard)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboTheme = QtGui.QComboBox(self.tab_2)
        self.comboTheme.setObjectName("comboTheme")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboTheme)
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.editBackground = QtGui.QLineEdit(self.tab_2)
        self.editBackground.setObjectName("editBackground")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.editBackground)
        self.buttonBrowse = QtGui.QPushButton(self.tab_2)
        self.buttonBrowse.setObjectName("buttonBrowse")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.buttonBrowse)
        self.graphicsView = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView.setObjectName("graphicsView")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.graphicsView)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Greeter", None, QtGui.QApplication.UnicodeUTF8))
        self.checkNumlock.setText(QtGui.QApplication.translate("MainWindow", "Numlock", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "GTK Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.checkShowBottomPanel.setText(QtGui.QApplication.translate("MainWindow", "Show bottom panel", None, QtGui.QApplication.UnicodeUTF8))
        self.checkShowLanguageSelector.setText(QtGui.QApplication.translate("MainWindow", "Show language selector", None, QtGui.QApplication.UnicodeUTF8))
        self.checkShowKeyboard.setText(QtGui.QApplication.translate("MainWindow", "Show keyboard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Background", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBrowse.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

