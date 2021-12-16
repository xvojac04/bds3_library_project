import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f

class DeleteBook(QtWidgets.QMainWindow):
    def __init__(self):
        super(DeleteBook, self).__init__()
        uic.loadUi('delete_book_main_window.ui', self)
        self.setWindowTitle("Delete Book")

        self.id_input = self.findChild(QtWidgets.QLineEdit, "id_input")

        self.enter_button = self.findChild(QtWidgets.QPushButton, "enter_button")
        self.enter_button.clicked.connect(self.enterButtonPressed)


        self.show()

    def enterButtonPressed(self):
        #print("Button is pressed")
        f.bookDelete(self.title_input.text())
        self.close()

def deleteBookWindowRun():
    app = QtWidgets.QApplication(sys.argv)
    window = DeleteBook()
    app.exec_()


if __name__ == "__main__":
    deleteBookWindowRun()