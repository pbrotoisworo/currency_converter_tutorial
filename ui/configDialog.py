# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 166)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 171, 41))
        self.label_2.setObjectName("label_2")
        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(100, 120, 93, 28))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonClose = QtWidgets.QPushButton(Dialog)
        self.pushButtonClose.setGeometry(QtCore.QRect(210, 120, 93, 28))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.comboBoxDefaultReferenceCurrency = QtWidgets.QComboBox(Dialog)
        self.comboBoxDefaultReferenceCurrency.setGeometry(QtCore.QRect(200, 70, 73, 22))
        self.comboBoxDefaultReferenceCurrency.setObjectName("comboBoxDefaultReferenceCurrency")
        self.comboBoxDefaultReferenceCurrency.addItem("")
        self.comboBoxDefaultReferenceCurrency.addItem("")
        self.comboBoxDefaultReferenceCurrency.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Configure Settings"))
        self.label_2.setText(_translate("Dialog", "Default Reference Currency"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonClose.setText(_translate("Dialog", "Close"))
        self.comboBoxDefaultReferenceCurrency.setItemText(0, _translate("Dialog", "USD"))
        self.comboBoxDefaultReferenceCurrency.setItemText(1, _translate("Dialog", "PHP"))
        self.comboBoxDefaultReferenceCurrency.setItemText(2, _translate("Dialog", "IDR"))
