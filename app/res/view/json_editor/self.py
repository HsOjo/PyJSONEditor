# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JSONEditor(object):
    def setupUi(self, JSONEditor):
        JSONEditor.setObjectName("JSONEditor")
        JSONEditor.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(JSONEditor)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tw_content = QtWidgets.QTreeWidget(JSONEditor)
        self.tw_content.setTabKeyNavigation(True)
        self.tw_content.setAlternatingRowColors(True)
        self.tw_content.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_content.setAnimated(True)
        self.tw_content.setAllColumnsShowFocus(True)
        self.tw_content.setWordWrap(False)
        self.tw_content.setExpandsOnDoubleClick(False)
        self.tw_content.setObjectName("tw_content")
        self.horizontalLayout.addWidget(self.tw_content)

        self.retranslateUi(JSONEditor)
        QtCore.QMetaObject.connectSlotsByName(JSONEditor)

    def retranslateUi(self, JSONEditor):
        _translate = QtCore.QCoreApplication.translate
        JSONEditor.setWindowTitle(_translate("JSONEditor", "JSONEditor"))
        self.tw_content.headerItem().setText(0, _translate("JSONEditor", "key"))
        self.tw_content.headerItem().setText(1, _translate("JSONEditor", "type"))
        self.tw_content.headerItem().setText(2, _translate("JSONEditor", "value"))
