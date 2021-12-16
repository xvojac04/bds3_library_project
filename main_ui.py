import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget



class SignInScreen(QDialog):
    def __init__(self):
        super(SignInScreen, self).__init__()
        loadUi("sign_in_dialog.ui", self)


# ===============================main=======================================================
app = QApplication(sys.argv)
sign_in = SignInScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(sign_in)
widget.show()

try:
    sys.exit(app_exec())
except:
    print("Exiting")
