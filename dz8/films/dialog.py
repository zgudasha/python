# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 413)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.title = QtWidgets.QTextEdit(Form)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.year = QtWidgets.QTextEdit(Form)
        self.year.setObjectName("year")
        self.verticalLayout_2.addWidget(self.year)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.genre = QtWidgets.QTextEdit(Form)
        self.genre.setObjectName("genre")
        self.verticalLayout_3.addWidget(self.genre)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.duration = QtWidgets.QTextEdit(Form)
        self.duration.setObjectName("duration")
        self.verticalLayout_4.addWidget(self.duration)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 2, 0, 1, 1)
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Год"))
        self.label_3.setText(_translate("Form", "Жанр"))
        self.label_4.setText(_translate("Form", "Продолжительность"))
        self.ok.setText(_translate("Form", "ok"))
        self.cancel.setText(_translate("Form", "cancel"))
