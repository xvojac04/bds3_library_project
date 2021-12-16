import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f

class FindBook(QtWidgets.QMainWindow):
    def __init__(self, table):
        super(FindBook, self).__init__()
        uic.loadUi('find_book_main_window.ui', self)
        self.setWindowTitle("Find Book")
        self.table = table
        self.title_input = self.findChild(QtWidgets.QLineEdit, "title_input")


        self.enter_button = self.findChild(QtWidgets.QPushButton, "enter_button")
        self.enter_button.clicked.connect(self.enterButtonPressed)


        self.show()

    def enterButtonPressed(self):
        #print("Button is pressed")
        results = f.findBook(self.title_input.text())
        self.table.setColumnWidth(0, 135)
        self.table.setColumnWidth(1, 136)
        self.table.setColumnWidth(2, 136)
        self.table.setColumnWidth(3, 135)

        self.table.setRowCount(len(results) if results else 0)

        tablerow = 0
        if results:
            for row in results:
                self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                tablerow = tablerow + 1
        self.close()

def findBookWindowRun():
    app = QtWidgets.QApplication(sys.argv)
    window = FindBook()
    app.exec_()


if __name__ == "__main__":
    findBookWindowRun()