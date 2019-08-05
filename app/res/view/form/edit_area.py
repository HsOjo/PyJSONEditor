# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_area.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 487)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.gb_area_edit = QtWidgets.QGroupBox(Form)
        self.gb_area_edit.setObjectName("gb_area_edit")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gb_area_edit)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_raw_data = QtWidgets.QLabel(self.gb_area_edit)
        self.l_raw_data.setObjectName("l_raw_data")
        self.verticalLayout.addWidget(self.l_raw_data)
        self.pte_raw = QtWidgets.QPlainTextEdit(self.gb_area_edit)
        self.pte_raw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pte_raw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.pte_raw.setObjectName("pte_raw")
        self.verticalLayout.addWidget(self.pte_raw)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.l_translate = QtWidgets.QLabel(self.gb_area_edit)
        self.l_translate.setObjectName("l_translate")
        self.gridLayout_3.addWidget(self.l_translate, 0, 0, 1, 1)
        self.cb_lang_to = QtWidgets.QComboBox(self.gb_area_edit)
        self.cb_lang_to.setObjectName("cb_lang_to")
        self.gridLayout_3.addWidget(self.cb_lang_to, 0, 2, 1, 1)
        self.pb_translate = QtWidgets.QPushButton(self.gb_area_edit)
        self.pb_translate.setObjectName("pb_translate")
        self.gridLayout_3.addWidget(self.pb_translate, 1, 2, 1, 1)
        self.cb_lang_from = QtWidgets.QComboBox(self.gb_area_edit)
        self.cb_lang_from.setObjectName("cb_lang_from")
        self.gridLayout_3.addWidget(self.cb_lang_from, 0, 1, 1, 1)
        self.cb_translator = QtWidgets.QComboBox(self.gb_area_edit)
        self.cb_translator.setObjectName("cb_translator")
        self.gridLayout_3.addWidget(self.cb_translator, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.l_current_data = QtWidgets.QLabel(self.gb_area_edit)
        self.l_current_data.setObjectName("l_current_data")
        self.verticalLayout_2.addWidget(self.l_current_data)
        self.pte_current_data = QtWidgets.QPlainTextEdit(self.gb_area_edit)
        self.pte_current_data.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pte_current_data.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.pte_current_data.setObjectName("pte_current_data")
        self.verticalLayout_2.addWidget(self.pte_current_data)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_reset = QtWidgets.QPushButton(self.gb_area_edit)
        self.pb_reset.setObjectName("pb_reset")
        self.horizontalLayout.addWidget(self.pb_reset)
        self.pb_save = QtWidgets.QPushButton(self.gb_area_edit)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout.addWidget(self.pb_save)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.gb_area_edit, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_area_edit.setTitle(_translate("Form", "area_edit"))
        self.l_raw_data.setText(_translate("Form", "raw_data"))
        self.l_translate.setText(_translate("Form", "translate"))
        self.pb_translate.setText(_translate("Form", "translate"))
        self.l_current_data.setText(_translate("Form", "current_data"))
        self.pb_reset.setText(_translate("Form", "reset"))
        self.pb_save.setText(_translate("Form", "save"))

