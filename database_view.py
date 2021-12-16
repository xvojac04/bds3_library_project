import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMessageBox
import functions as f
from new_book import NewBook
from update_book import UpdateBook
from new_tryme import NewTryMe
from find_book import FindBook
from delete_book import DeleteBook

class ViewTable(QtWidgets.QMainWindow):
    def __init__(self):
        super(ViewTable, self).__init__()
        uic.loadUi('main_window.ui', self)
        self.w = None
        self.setWindowTitle("Library Database")

        self.books_button = self.findChild(QtWidgets.QPushButton, "books_button")
        self.books_button.clicked.connect(self.booksButtonPressed)

        self.borrow_button = self.findChild(QtWidgets.QPushButton, "borrow_button")
        self.borrow_button.clicked.connect(self.borrowButtonPressed)

        self.try_me_button = self.findChild(QtWidgets.QPushButton, "try_me_button")
        self.try_me_button.clicked.connect(self.trymeButtonPressed)

        self.new_button = self.findChild(QtWidgets.QPushButton, "new_button")
        self.new_button.clicked.connect(self.newButtonPressed)

        self.update_button = self.findChild(QtWidgets.QPushButton, "update_button")
        self.update_button.clicked.connect(self.updateButtonPressed)

        self.find_button = self.findChild(QtWidgets.QPushButton, "find_button")
        self.find_button.clicked.connect(self.findButtonPressed)

        self.delete_button = self.findChild(QtWidgets.QPushButton, "delete_button")
        self.delete_button.clicked.connect(self.deleteButtonPressed)

        self.sql_button = self.findChild(QtWidgets.QPushButton, "sql_button")
        self.sql_button.clicked.connect(self.sqlButtonPressed)

        self.show()

    def booksButtonPressed(self):
        print("Button book is pressed")
        self.stackedWidget.setCurrentWidget(self.page_book)

        self.books_tableWidget.setColumnWidth(0, 135)
        self.books_tableWidget.setColumnWidth(1, 136)
        self.books_tableWidget.setColumnWidth(2, 136)
        self.books_tableWidget.setColumnWidth(3, 135)

        book_records = f.getBookRows()

        self.books_tableWidget.setRowCount(len(book_records) if book_records else 0)

        tablerow = 0
        if book_records:
            for row in book_records:
                self.books_tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.books_tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.books_tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.books_tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                tablerow = tablerow + 1


    def borrowButtonPressed(self):
        print("Button borrow is pressed")
        self.stackedWidget.setCurrentWidget(self.page_borrow)
        self.borrow_tableWidget.setColumnWidth(0, 133)
        self.borrow_tableWidget.setColumnWidth(1, 120)
        self.borrow_tableWidget.setColumnWidth(2, 120)
        self.borrow_tableWidget.setColumnWidth(3, 85)
        self.borrow_tableWidget.setColumnWidth(4, 85)

        borrow_records = f.getBorrowRows()

        self.borrow_tableWidget.setRowCount(len(borrow_records) if borrow_records else 0)

        tablerow = 0
        if borrow_records:
            for row in borrow_records:
                self.borrow_tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.borrow_tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.borrow_tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.borrow_tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3].strftime("%Y-%m-%d %H:%M")))
                self.borrow_tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4].strftime("%Y-%m-%d %H:%M")))
                tablerow = tablerow + 1

    def trymeButtonPressed(self):
        print("Button tryme is pressed")
        self.stackedWidget.setCurrentWidget(self.page_tryme)
        self.try_me_tableWidget.setColumnWidth(0, 175)
        self.try_me_tableWidget.setColumnWidth(1, 175)
        self.try_me_tableWidget.setColumnWidth(2, 193)

        tryme_records = f.getTrymeRows()

        self.try_me_tableWidget.setRowCount(len(tryme_records) if tryme_records else 0)

        tablerow = 0
        if tryme_records:
            for row in tryme_records:
                self.try_me_tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.try_me_tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.try_me_tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tablerow = tablerow + 1

    def newButtonPressed(self):
        print("Button new is pressed")
        print("Open new window for new book record")
        self.w = NewBook()
        self.w.show()


    def updateButtonPressed(self):
        print("Button update is pressed")
        print("Open new window for update book record")
        self.w = UpdateBook()
        self.w.show()


    def findButtonPressed(self):
        print("Button find is pressed")
        print("Open new window for find book record")
        self.stackedWidget.setCurrentWidget(self.page_find)
        self.w = FindBook(self.find_tableWidget)
        self.w.show()

    def deleteButtonPressed(self):
        print("Button delete is pressed")
        print("Open new window for delete book record")
        self.w = DeleteBook()
        self.w.show()

    def sqlButtonPressed(self):
        print("Button for SQL injection is pressed")
        print("Open new window for sql injection book record")
        self.w = NewTryMe()
        self.w.show()



def DatabaseWindowRun():
    app = QtWidgets.QApplication(sys.argv)
    window = ViewTable()
    app.exec_()


if __name__ == "__main__":
    DatabaseWindowRun()
