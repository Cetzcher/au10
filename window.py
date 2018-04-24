# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 4, 1, 1)
        self.portInp = QtWidgets.QLineEdit(self.centralwidget)
        self.portInp.setObjectName("portInp")
        self.gridLayout.addWidget(self.portInp, 0, 5, 1, 1)
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setObjectName("resetBtn")
        self.gridLayout.addWidget(self.resetBtn, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.checkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.checkBtn.setObjectName("checkBtn")
        self.gridLayout.addWidget(self.checkBtn, 5, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 6)
        self.hostInp = QtWidgets.QLineEdit(self.centralwidget)
        self.hostInp.setObjectName("hostInp")
        self.gridLayout.addWidget(self.hostInp, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 6, 1, 1)
        self.inpText = QtWidgets.QTextEdit(self.centralwidget)
        self.inpText.setObjectName("inpText")
        self.gridLayout.addWidget(self.inpText, 2, 0, 1, 7)
        self.outTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.outTxt.setEnabled(True)
        self.outTxt.setObjectName("outTxt")
        self.gridLayout.addWidget(self.outTxt, 4, 0, 1, 7)
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout.addWidget(self.closeBtn, 5, 5, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        self.resetBtn.setText(_translate("MainWindow", "reset"))
        self.label_3.setText(_translate("MainWindow", "HOST"))
        self.checkBtn.setText(_translate("MainWindow", "check"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.label_4.setText(_translate("MainWindow", "PORT"))
        self.label.setText(_translate("MainWindow", "Input Text"))
        self.closeBtn.setText(_translate("MainWindow", "close"))

