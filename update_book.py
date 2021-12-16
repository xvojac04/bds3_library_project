import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f

class UpdateBook(QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateBook, self).__init__()
        uic.loadUi('update_book_main_window.ui', self)
        self.setWindowTitle("Update Book")

        self.title_input = self.findChild(QtWidgets.QLineEdit, "title_input")
        self.id_input = self.findChild(QtWidgets.QLineEdit, "id_input")

        self.enter_button = self.findChild(QtWidgets.QPushButton, "enter_button")
        self.enter_button.clicked.connect(self.enterButtonPressed)

        self.show()


    def enterButtonPressed(self):
        #print("Button is pressed")
        f.bookUpdate(self.title_input.text(), self.id_input.text())
        self.close()

def updateBookWindowRun():
    app = QtWidgets.QApplication(sys.argv)
    window = UpdateBook()
    app.exec_()


if __name__ == "__main__":
    updateBookWindowRun()