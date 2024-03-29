# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.m_edit = QtWidgets.QMenu(self.menubar)
        self.m_edit.setObjectName("m_edit")
        self.m_languages = QtWidgets.QMenu(self.menubar)
        self.m_languages.setObjectName("m_languages")
        self.m_view = QtWidgets.QMenu(self.menubar)
        self.m_view.setObjectName("m_view")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.a_open_file = QtWidgets.QAction(MainWindow)
        self.a_open_file.setObjectName("a_open_file")
        self.a_close = QtWidgets.QAction(MainWindow)
        self.a_close.setObjectName("a_close")
        self.a_save_file = QtWidgets.QAction(MainWindow)
        self.a_save_file.setObjectName("a_save_file")
        self.a_close_file = QtWidgets.QAction(MainWindow)
        self.a_close_file.setObjectName("a_close_file")
        self.a_undo = QtWidgets.QAction(MainWindow)
        self.a_undo.setObjectName("a_undo")
        self.a_redo = QtWidgets.QAction(MainWindow)
        self.a_redo.setObjectName("a_redo")
        self.a_copy = QtWidgets.QAction(MainWindow)
        self.a_copy.setObjectName("a_copy")
        self.a_paste = QtWidgets.QAction(MainWindow)
        self.a_paste.setObjectName("a_paste")
        self.a_cut = QtWidgets.QAction(MainWindow)
        self.a_cut.setObjectName("a_cut")
        self.a_find = QtWidgets.QAction(MainWindow)
        self.a_find.setObjectName("a_find")
        self.a_replace = QtWidgets.QAction(MainWindow)
        self.a_replace.setObjectName("a_replace")
        self.a_new_file = QtWidgets.QAction(MainWindow)
        self.a_new_file.setObjectName("a_new_file")
        self.a_previous_file = QtWidgets.QAction(MainWindow)
        self.a_previous_file.setObjectName("a_previous_file")
        self.a_next_file = QtWidgets.QAction(MainWindow)
        self.a_next_file.setObjectName("a_next_file")
        self.a_save_file_as = QtWidgets.QAction(MainWindow)
        self.a_save_file_as.setObjectName("a_save_file_as")
        self.a_save_file_all = QtWidgets.QAction(MainWindow)
        self.a_save_file_all.setObjectName("a_save_file_all")
        self.m_file.addAction(self.a_new_file)
        self.m_file.addAction(self.a_open_file)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_save_file)
        self.m_file.addAction(self.a_save_file_as)
        self.m_file.addAction(self.a_save_file_all)
        self.m_file.addSeparator()
        self.m_file.addAction(self.a_close_file)
        self.m_edit.addAction(self.a_undo)
        self.m_edit.addAction(self.a_redo)
        self.m_edit.addSeparator()
        self.m_edit.addAction(self.a_cut)
        self.m_edit.addAction(self.a_copy)
        self.m_edit.addAction(self.a_paste)
        self.m_edit.addSeparator()
        self.m_edit.addAction(self.a_find)
        self.m_edit.addAction(self.a_replace)
        self.m_view.addAction(self.a_previous_file)
        self.m_view.addAction(self.a_next_file)
        self.menubar.addAction(self.m_file.menuAction())
        self.menubar.addAction(self.m_edit.menuAction())
        self.menubar.addAction(self.m_view.menuAction())
        self.menubar.addAction(self.m_languages.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AppName"))
        self.m_file.setTitle(_translate("MainWindow", "file"))
        self.m_edit.setTitle(_translate("MainWindow", "edit"))
        self.m_languages.setTitle(_translate("MainWindow", "languages"))
        self.m_view.setTitle(_translate("MainWindow", "m_view"))
        self.a_open_file.setText(_translate("MainWindow", "open_file"))
        self.a_open_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.a_close.setText(_translate("MainWindow", "close"))
        self.a_close.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.a_save_file.setText(_translate("MainWindow", "save_file"))
        self.a_save_file.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.a_close_file.setText(_translate("MainWindow", "close_file"))
        self.a_close_file.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.a_undo.setText(_translate("MainWindow", "undo"))
        self.a_undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.a_redo.setText(_translate("MainWindow", "redo"))
        self.a_redo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.a_copy.setText(_translate("MainWindow", "copy"))
        self.a_copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.a_paste.setText(_translate("MainWindow", "paste"))
        self.a_paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.a_cut.setText(_translate("MainWindow", "cut"))
        self.a_cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.a_find.setText(_translate("MainWindow", "find"))
        self.a_find.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.a_replace.setText(_translate("MainWindow", "replace"))
        self.a_replace.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.a_new_file.setText(_translate("MainWindow", "new_file"))
        self.a_new_file.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.a_previous_file.setText(_translate("MainWindow", "a_previous_file"))
        self.a_previous_file.setShortcut(_translate("MainWindow", "Ctrl+["))
        self.a_next_file.setText(_translate("MainWindow", "a_next_file"))
        self.a_next_file.setShortcut(_translate("MainWindow", "Ctrl+]"))
        self.a_save_file_as.setText(_translate("MainWindow", "save_file_as"))
        self.a_save_file_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.a_save_file_all.setText(_translate("MainWindow", "save_file_all"))
        self.a_save_file_all.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
