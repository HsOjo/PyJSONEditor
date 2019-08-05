# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_content = QtWidgets.QTabWidget(self.centralwidget)
        self.tw_content.setObjectName("tw_content")
        self.gridLayout.addWidget(self.tw_content, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.m_file = QtWidgets.QMenu(self.menubar)
        self.m_file.setObjectName("m_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.a_open_file = QtWidgets.QAction(MainWindow)
        self.a_open_file.setObjectName("a_open_file")
        self.a_model = QtWidgets.QAction(MainWindow)
        self.a_model.setObjectName("a_model")
        self.a_close = QtWidgets.QAction(MainWindow)
        self.a_close.setObjectName("a_close")
        self.a_save_file = QtWidgets.QAction(MainWindow)
        self.a_save_file.setObjectName("a_save_file")
        self.a_close_file = QtWidgets.QAction(MainWindow)
        self.a_close_file.setObjectName("a_close_file")
        self.m_file.addAction(self.a_open_file)
        self.m_file.addAction(self.a_save_file)
        self.m_file.addAction(self.a_close_file)
        self.menubar.addAction(self.m_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AppName"))
        self.m_file.setTitle(_translate("MainWindow", "文件"))
        self.a_open_file.setText(_translate("MainWindow", "open_file"))
        self.a_open_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.a_model.setText(_translate("MainWindow", "模型"))
        self.a_model.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.a_close.setText(_translate("MainWindow", "关闭"))
        self.a_close.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.a_save_file.setText(_translate("MainWindow", "save_file"))
        self.a_close_file.setText(_translate("MainWindow", "close_file"))

