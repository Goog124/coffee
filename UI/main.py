# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kza4\PycharmProjects\coffee\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Coffee(object):
    def setupUi(self, Coffee):
        Coffee.setObjectName("Coffee")
        Coffee.resize(800, 493)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Coffee.sizePolicy().hasHeightForWidth())
        Coffee.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Coffee)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 409, 791, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.show_button.setFont(font)
        self.show_button.setObjectName("show_button")
        self.horizontalLayout.addWidget(self.show_button)
        self.add_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.update_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.update_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.horizontalLayout.addWidget(self.update_button)
        self.delete_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        Coffee.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Coffee)
        self.statusbar.setObjectName("statusbar")
        Coffee.setStatusBar(self.statusbar)

        self.retranslateUi(Coffee)
        QtCore.QMetaObject.connectSlotsByName(Coffee)

    def retranslateUi(self, Coffee):
        _translate = QtCore.QCoreApplication.translate
        Coffee.setWindowTitle(_translate("Coffee", "Кофейный список"))
        self.show_button.setText(_translate("Coffee", "Показать список кофе"))
        self.add_button.setText(_translate("Coffee", "Добавить кофе"))
        self.update_button.setText(_translate("Coffee", "Изменить"))
        self.delete_button.setText(_translate("Coffee", "Удалить"))
