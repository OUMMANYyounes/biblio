from PyQt5 import QtCore, QtGui, QtWidgets

####################################################################################################
import sqlite3  
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel,QSqlQuery
from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import subprocess
from PyQt5.QtWidgets import QMessageBox
####################################################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_displayguest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_displayguest.setGeometry(QtCore.QRect(420, 120, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_displayguest.setFont(font)
        self.pushButton_displayguest.setObjectName("pushButton_displayguest")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(148, 30, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 82, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_reservation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reservation.setGeometry(QtCore.QRect(80, 120, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_reservation.setFont(font)
        self.pushButton_reservation.setObjectName("pushButton_reservation")
        self.label_reservation_error = QtWidgets.QLabel(self.centralwidget)
        self.label_reservation_error.setGeometry(QtCore.QRect(80, 120, 291, 20))
        self.label_reservation_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_reservation_error.setText("")
        self.label_reservation_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reservation_error.setObjectName("label_reservation_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#############################################################################################################
        self.pushButton_displayguest.clicked.connect(self.show_all)
        self.pushButton_reservation.clicked.connect(self.res)
#############################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_displayguest.setText(_translate("MainWindow", "DISPLAY \n"
"ALL"))
        self.label_3.setText(_translate("MainWindow", "Enter the id or the Title of the book you want \n"
"to reserve :"))
        self.pushButton_reservation.setText(_translate("MainWindow", "MAKE \n"
"THE RESERVATION"))

#############################################################################################################################################
    def show_all(self):
        MainWindow.close()
        subprocess.run(["python", "show_all_guest.py"])

    def res(self):
        self.lineEdit.clear()

        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        msg.setText("Order has been placed successfully")
        x = msg.exec_()

#############################################################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

subprocess.run(["python", "login.py"])