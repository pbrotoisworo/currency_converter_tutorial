from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui.mainDialog as mainDialog
import ui.configDialog as configDialog

import sys
import requests
import pickle
import os

global CONFIG_FILE
CONFIG_FILE = 'config.pkl'


class ConfigParameters(QDialog, configDialog.Ui_Dialog):

    def __init__(self, parent=None):
        super(ConfigParameters, self).__init__(parent)
        self.setupUi(self)

        with open(CONFIG_FILE, 'rb') as f:
            self.config = pickle.load(f)

        self.comboBoxDefaultReferenceCurrency.setCurrentText(self.config['ref_currency'])

        self.pushButtonSave.clicked.connect(self.update_config)
        self.pushButtonClose.clicked.connect(self.close_window)

    def update_config(self):

        self.config['ref_currency'] = self.comboBoxDefaultReferenceCurrency.currentText()

        with open(CONFIG_FILE, 'wb') as f:
            pickle.dump(self.config, f)

    def close_window(self):
        self.close()


class MainDialog(QDialog, mainDialog.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'rb') as f:
                self.config = pickle.load(f)
        else:
            with open(CONFIG_FILE, 'wb') as f:
                self.config = {'ref_currency': 'USD'}
                pickle.dump(self.config, f)

        pixmap = QPixmap('ui/logo.JPG')
        self.labelLogo.setPixmap(pixmap)
        self.labelLogo.setScaledContents(True)

        self.comboBoxReferenceCurrency.setCurrentText(self.config['ref_currency'])

        self.pushButtonLoadRates.clicked.connect(self.load_rates)
        self.pushButtonConfigure.clicked.connect(self.open_config_window)

    def open_config_window(self):
        self.configParameters = ConfigParameters(self)
        self.configParameters.exec_()

        with open(CONFIG_FILE, 'rb') as f:
            self.config = pickle.load(f)

        self.comboBoxReferenceCurrency.setCurrentText(self.config['ref_currency'])

    def load_rates(self):
        reference = self.comboBoxReferenceCurrency.currentText()
        url = 'https://api.exchangerate-api.com/v4/latest/' + reference
        response = requests.get(url)
        data = response.json()

        self.lineEditIDR.setText(str(data['rates']['IDR']))
        self.lineEditPHP.setText(str(data['rates']['PHP']))
        self.lineEditUSD.setText(str(data['rates']['USD']))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()
