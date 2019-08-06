# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(928, 673)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tw_content = QtWidgets.QTreeWidget(Form)
        self.tw_content.setTabKeyNavigation(True)
        self.tw_content.setAlternatingRowColors(True)
        self.tw_content.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_content.setAnimated(True)
        self.tw_content.setAllColumnsShowFocus(True)
        self.tw_content.setWordWrap(False)
        self.tw_content.setExpandsOnDoubleClick(False)
        self.tw_content.setObjectName("tw_content")
        self.horizontalLayout.addWidget(self.tw_content)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tw_content.headerItem().setText(0, _translate("Form", "key"))
        self.tw_content.headerItem().setText(1, _translate("Form", "type"))
        self.tw_content.headerItem().setText(2, _translate("Form", "value"))

