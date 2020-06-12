# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'films.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 780)
        MainWindow.setStyleSheet("background-color: rgb(255, 226, 227)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.titleField = QtWidgets.QTextEdit(self.centralwidget)
        self.titleField.setStyleSheet("background-color: rgba(241, 217, 255, 100);")
        self.titleField.setObjectName("titleField")
        self.verticalLayout.addWidget(self.titleField)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.yearField = QtWidgets.QTextEdit(self.centralwidget)
        self.yearField.setStyleSheet("background-color: rgba(241, 217, 255, 100);")
        self.yearField.setObjectName("yearField")
        self.verticalLayout_2.addWidget(self.yearField)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.durationField = QtWidgets.QTextEdit(self.centralwidget)
        self.durationField.setStyleSheet("background-color: rgba(241, 217, 255, 100);\n"
"")
        self.durationField.setObjectName("durationField")
        self.verticalLayout_4.addWidget(self.durationField)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.list.setStyleSheet("background-color: rgba(241, 217, 255, 100);")
        self.list.setObjectName("list")
        self.verticalLayout_5.addWidget(self.list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setStyleSheet("background-color: rgba(241, 217, 255, 100);\n"
"border: 1px solid #000;\n"
"padding: 10px;")
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout_3.addWidget(self.btnSearch)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setStyleSheet("background-color: rgba(241, 217, 255, 100);\n"
"border: 1px solid #000;\n"
"padding: 10px;")
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_3.addWidget(self.btnSave)
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setStyleSheet("background-color: rgba(241, 217, 255, 100);\n"
"border: 1px solid #000;\n"
"padding: 10px;\n"
"")
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_3.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemove.setStyleSheet("background-color: rgba(241, 217, 255, 100);\n"
"border: 1px solid #000;\n"
"padding: 10px;")
        self.btnRemove.setObjectName("btnRemove")
        self.horizontalLayout_3.addWidget(self.btnRemove)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setStyleSheet("background-color: rgba(241, 217, 255, 100);")
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.titleField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Год"))
        self.yearField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Продолжительность"))
        self.durationField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.btnSearch.setText(_translate("MainWindow", "поиск"))
        self.btnSave.setText(_translate("MainWindow", "сохранить"))
        self.btnAdd.setText(_translate("MainWindow", "добавить фильм"))
        self.btnRemove.setText(_translate("MainWindow", "удалить"))
