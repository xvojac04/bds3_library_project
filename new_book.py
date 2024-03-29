import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f
from logger import setup_logger
import logging

setup_logger('log2', "input.log")
logger_2 = logging.getLogger('log2')


class NewBook(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewBook, self).__init__()
        uic.loadUi('new_book_main_window.ui', self)
        self.setWindowTitle("New Book")

        self.title_input = self.findChild(QtWidgets.QLineEdit, "title_input")
        self.name_input = self.findChild(QtWidgets.QLineEdit, "name_input")
        self.surname_input = self.findChild(QtWidgets.QLineEdit, "surname_input")

        self.enter_button = self.findChild(QtWidgets.QPushButton, "enter_button")
        self.enter_button.clicked.connect(self.enterButtonPressed)


        self.show()

    def enterButtonPressed(self):
        #print("Button is pressed")
        #logger2.warning(f"New insert: {self.title_input.text(), self.name_input.text(), self.surname_input.text()}")
        logger_2.warning(f"New insert book: {self.title_input.text(), self.name_input.text(), self.surname_input.text()}")
        f.insertNewBook(self.title_input.text(), self.name_input.text(), self.surname_input.text())
        self.close()

def newBookWindowRun():
    app = QtWidgets.QApplication(sys.argv)
    window = NewBook()
    app.exec_()


if __name__ == "__main__":
    newBookWindowRun()