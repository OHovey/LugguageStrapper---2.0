# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 551))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout_2.addWidget(self.add_button)
        self.edit_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.edit_button.setObjectName("edit_button")
        self.verticalLayout_2.addWidget(self.edit_button)
        self.delete_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_2.addWidget(self.delete_button)
        self.red_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.red_button.setObjectName("red_button")
        self.verticalLayout_2.addWidget(self.red_button)
        self.blue_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.blue_button.setObjectName("blue_button")
        self.verticalLayout_2.addWidget(self.blue_button)
        self.papertime_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.papertime_button.setObjectName("papertime_button")
        self.verticalLayout_2.addWidget(self.papertime_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(259, -1, 531, 551))
        self.widget.setObjectName("widget")
        self.strap_table = QtWidgets.QTableWidget(self.widget)
        self.strap_table.setGeometry(QtCore.QRect(0, 0, 501, 561))
        self.strap_table.setObjectName("strap_table")
        self.strap_table.setColumnCount(0)
        self.strap_table.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 21))
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
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.edit_button.setText(_translate("MainWindow", "Edit"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.red_button.setText(_translate("MainWindow", "Red (.bmp)"))
        self.blue_button.setText(_translate("MainWindow", "Blue (.jc5)"))
        self.papertime_button.setText(_translate("MainWindow", "Papertime"))
