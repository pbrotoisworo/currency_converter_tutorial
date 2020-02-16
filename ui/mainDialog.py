# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 340)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelUSD = QtWidgets.QLabel(Dialog)
        self.labelUSD.setGeometry(QtCore.QRect(95, 189, 24, 16))
        self.labelUSD.setObjectName("labelUSD")
        self.labelPHP = QtWidgets.QLabel(Dialog)
        self.labelPHP.setGeometry(QtCore.QRect(95, 218, 22, 16))
        self.labelPHP.setObjectName("labelPHP")
        self.labelIDR = QtWidgets.QLabel(Dialog)
        self.labelIDR.setGeometry(QtCore.QRect(95, 247, 20, 16))
        self.labelIDR.setObjectName("labelIDR")
        self.lineEditUSD = QtWidgets.QLineEdit(Dialog)
        self.lineEditUSD.setGeometry(QtCore.QRect(160, 189, 137, 22))
        self.lineEditUSD.setObjectName("lineEditUSD")
        self.lineEditPHP = QtWidgets.QLineEdit(Dialog)
        self.lineEditPHP.setGeometry(QtCore.QRect(160, 218, 137, 22))
        self.lineEditPHP.setObjectName("lineEditPHP")
        self.lineEditIDR = QtWidgets.QLineEdit(Dialog)
        self.lineEditIDR.setGeometry(QtCore.QRect(160, 247, 137, 22))
        self.lineEditIDR.setObjectName("lineEditIDR")
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(260, 20, 101, 101))
        self.labelLogo.setObjectName("labelLogo")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(95, 160, 58, 16))
        self.label_2.setObjectName("label_2")
        self.comboBoxReferenceCurrency = QtWidgets.QComboBox(Dialog)
        self.comboBoxReferenceCurrency.setGeometry(QtCore.QRect(160, 160, 73, 22))
        self.comboBoxReferenceCurrency.setObjectName("comboBoxReferenceCurrency")
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.addItem("")
        self.comboBoxReferenceCurrency.addItem("")
        self.pushButtonConfigure = QtWidgets.QPushButton(Dialog)
        self.pushButtonConfigure.setGeometry(QtCore.QRect(90, 290, 93, 28))
        self.pushButtonConfigure.setObjectName("pushButtonConfigure")
        self.pushButtonLoadRates = QtWidgets.QPushButton(Dialog)
        self.pushButtonLoadRates.setGeometry(QtCore.QRect(190, 290, 93, 28))
        self.pushButtonLoadRates.setObjectName("pushButtonLoadRates")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Currency Converter"))
        self.labelUSD.setText(_translate("Dialog", "USD"))
        self.labelPHP.setText(_translate("Dialog", "PHP"))
        self.labelIDR.setText(_translate("Dialog", "IDR"))
        self.labelLogo.setText(_translate("Dialog", "Logo"))
        self.label_2.setText(_translate("Dialog", "Reference"))
        self.comboBoxReferenceCurrency.setItemText(0, _translate("Dialog", "USD"))
        self.comboBoxReferenceCurrency.setItemText(1, _translate("Dialog", "PHP"))
        self.comboBoxReferenceCurrency.setItemText(2, _translate("Dialog", "IDR"))
        self.pushButtonConfigure.setText(_translate("Dialog", "Configure"))
        self.pushButtonLoadRates.setText(_translate("Dialog", "Load Rates"))
