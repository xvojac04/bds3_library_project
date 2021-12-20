import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f
from logger import setup_logger
import logging

setup_logger('log3', "input.log")
logger_3 = logging.getLogger('log3')


class NewTryMe(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewTryMe, self).__init__()
        uic.loadUi('new_tryme_main_window.ui', self)
        self.setWindowTitle("New Try me")

        self.name_input = self.findChild(QtWidgets.QLineEdit, "name_input")
        self.surname_input = self.findChild(QtWidgets.QLineEdit, "surname_input")
        self.age_input = self.findChild(QtWidgets.QLineEdit, "age_input")
        self.city_input = self.findChild(QtWidgets.QLineEdit, "city_input")

        self.enter_button = self.findChild(QtWidgets.QPushButton, "enter_button")
        self.enter_button.clicked.connect(self.enterButtonPressed)

        self.show()

    def enterButtonPressed(self):
        print("Button is pressed")
        logger_3.warning(f"New insert: {self.name_input.text(), self.surname_input.text(), self.age_input.text(), self.city_input.text()}")
        f.injectionSQL(self.name_input.text(), self.surname_input.text(), self.age_input.text(), self.city_input.text())
        self.close()


def newTryMeWindowRun():
    app = QtWidgets.QApplication(sys.argv)
    window = NewTryMe()
    app.exec_()


if __name__ == "__main__":
    newTryMeWindowRun()