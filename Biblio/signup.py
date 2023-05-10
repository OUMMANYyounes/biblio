from PyQt5 import QtCore, QtGui, QtWidgets
############################################################################################
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sqlite3
import subprocess
############################################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(60, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(170, 110, 181, 21))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 470, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.lineEdit_adresse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_adresse.setGeometry(QtCore.QRect(150, 180, 201, 21))
        self.lineEdit_adresse.setObjectName("lineEdit_adresse")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(130, 250, 221, 21))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 320, 181, 21))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_conpass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_conpass.setGeometry(QtCore.QRect(170, 390, 181, 21))
        self.lineEdit_conpass.setObjectName("lineEdit_conpass")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 360, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_errorusername = QtWidgets.QLabel(self.centralwidget)
        self.label_errorusername.setGeometry(QtCore.QRect(180, 140, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_errorusername.setFont(font)
        self.label_errorusername.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_errorusername.setText("")
        self.label_errorusername.setAlignment(QtCore.Qt.AlignCenter)
        self.label_errorusername.setObjectName("label_errorusername")
        self.label_errorpassword = QtWidgets.QLabel(self.centralwidget)
        self.label_errorpassword.setGeometry(QtCore.QRect(180, 350, 151, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_errorpassword.setFont(font)
        self.label_errorpassword.setText("")
        self.label_errorpassword.setAlignment(QtCore.Qt.AlignCenter)
        self.label_errorpassword.setObjectName("label_errorpassword")
        self.label_errorconfirm = QtWidgets.QLabel(self.centralwidget)
        self.label_errorconfirm.setGeometry(QtCore.QRect(180, 420, 151, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_errorconfirm.setFont(font)
        self.label_errorconfirm.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_errorconfirm.setText("")
        self.label_errorconfirm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_errorconfirm.setObjectName("label_errorconfirm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
####################################################################################################
        self.lineEdit_username.textChanged.connect(self.clear_u)
        self.lineEdit_password.textChanged.connect(self.clear_p)
        self.lineEdit_conpass.textChanged.connect(self.clear_c)
        self.pushButton.clicked.connect(self.check_signup)


####################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Username :"))
        self.pushButton.setText(_translate("MainWindow", "SIGN UP   -->"))
        self.title.setText(_translate("MainWindow", "Create your account"))
        self.label_2.setText(_translate("MainWindow", "Adresse :"))
        self.label_3.setText(_translate("MainWindow", "Email :"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.label_5.setText(_translate("MainWindow", "Confirm \n"
"Password :"))
        
#####################################################################################################
    
    def clear_u(self):
        self.label_errorusername.setText("")
    
    def clear_p(self):
        self.label_errorpassword.setText("")
    
    def clear_c(self):
        self.label_errorconfirm.setText("")  
    
    def check_signup(self):        
        #grab the input
        username = self.lineEdit_username.text()
        adresse = self.lineEdit_adresse.text()
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        conpass = self.lineEdit_conpass.text()

        if len(username) == 0 or  len(password) == 0 or password != conpass :
            if len(username) == 0 :
                self.label_errorusername.setText("Don't leave the username blank")
            if len(password) == 0 :
                self.label_errorpassword.setText("Don't leave the password blank")
            if password != conpass :
                self.label_errorconfirm.setText("passwords do not match")
        else:        
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("users_info.db")
            if not db.open():
                print("Error: could not open database")
                return False

            query = QSqlQuery()
            query.prepare("INSERT INTO user (username, adresse, email, password) VALUES (:username, :address, :email, :password)")
            query.bindValue(":username", username)
            query.bindValue(":address", adresse)
            query.bindValue(":email", email)
            query.bindValue(":password", password)
            if not query.exec_():
                print("Error:", query.lastError().text())
                return False
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Notification")
                msg.setText("sign-in confirmed\nReturning to the log in page")
                x = msg.exec_()
                print("Welcome Abord")
                MainWindow.close()
                subprocess.run(["python", "login.py"])
            db.close()
               



##################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
