import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f
from database_view import ViewTable
import logging

logging.basicConfig(filename="library.log")
logger = logging.getLogger(__name__)


class SignIn(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignIn, self).__init__()
        uic.loadUi('sign_in_main_window.ui', self)

        self.setWindowTitle("Sign in")

        self.enter_button = self.findChild(QtWidgets.QPushButton, "enter_button")
        self.enter_button.clicked.connect(self.enterButtonPressed)

        self.username_input = self.findChild(QtWidgets.QLineEdit, "username_input")
        self.password_input = self.findChild(QtWidgets.QLineEdit, "password_input")

        self.show()

    def enterButtonPressed(self):
        #print("Button is pressed")
        #print("Username: " + self.username_input.text())
        #print("Password: " + self.password_input.text())

        value = f.getLogin(self.username_input.text(), self.password_input.text())
        if value:

            print("Open new window with database")
            self.w = ViewTable()
            self.w.show()
            self.close()

        else:
            print("Wrong")
            logger.warning(f"User {self.username_input.text()} tried to log in with wrong password!")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong username or password")
            msg.setInformativeText('Try it again and correct this time')
            msg.setWindowTitle("Error")
            msg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = SignIn()
app.exec_()